from flask import Flask, request, jsonify, make_response, send_from_directory
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from functools import wraps
from datetime import datetime, timedelta
from tinydb import TinyDB, Query
from flask_cors import CORS
import numpy as np
from sklearn import preprocessing
import json
from joblib import load
import os

# Setup Flask
app = Flask(__name__,static_url_path='', static_folder='dist')
CORS(app)
app.config['JWT_SECRET_KEY'] = "KEY"

# Decorator for verifying JWT
def token_required(f):
	@wraps(f)
	def decorated(*args,**kwargs):
		token = None
		if 'x-access-token' in request.headers:
			token = request.headers['x-access-token']
		if not token:
			return make_response(jsonify({"msg" : 'Token is missing !!'}), 401)
		try:
			data = jwt.decode(token,app.config['JWT_SECRET_KEY'],algorithms=["HS256"])
			User = Query()
			current_user = db.search(User["id"] == data["id"])[0]
		except:
			return make_response(jsonify({"msg" : "Invalid Token"}),401)
		return f(current_user,*args,**kwargs)
	return decorated

# Predict
@app.route("/predict",methods=["POST"])
@token_required
def predict(current_user):
	# get data of indeces
	indeces = request.json
	
	# make the input arr
	zeros = np.zeros((322,)).astype(np.int64)
	np.put(zeros,indeces,1)
	inp = np.expand_dims(zeros,axis=0)

	# Make Prediction
	pred = clf.predict_proba(inp)
	sort_ind = np.argsort(pred)
	int_ind = sort_ind[0,-15:][::-1]
	high_prob = []
	low_prob = []
	other_prob = []
	for i in int_ind:
		prob = pred[0][i]
		if prob >= 0.8:
			high_prob.append(lb.inverse_transform([i])[0])
		elif (prob < 0.8 and prob > 0.5):
			low_prob.append(lb.inverse_transform([i])[0])
		elif (prob <= 0.5 and prob > 0):
			other_prob.append(lb.inverse_transform([i])[0])
	if len(high_prob) == 0 and len(low_prob) == 0:
		if len(indeces) < 3:
			return jsonify({ "code": "warning", "msg": "Decision Inconclusive, Try Adding more symptoms", "inconclusive": other_prob})
		else:
			return jsonify({ "code": "error", "msg": "Decision Inconclusive", "inconclusive": other_prob})
	else:
		return jsonify({"code": "success", "msg": "Most Probable", "high_rec": high_prob, "rec": low_prob})

# Signup
@app.route('/signup',methods=["POST"])
def signup():
	data = request.json
	User = Query()
	user = db.search(User["email"] == data["email"])
	if len(user) == 0:
		db.insert({
			"id": str(uuid.uuid4()),
			"name": data["name"].lower().replace(" ","_"),
			"email": data["email"],
			"password": generate_password_hash(data["password"])
		})
		resp = make_response(jsonify({"msg":'Successfully registered.'}),201)
		resp.headers["Content-Type"] = "application/json"
		return resp
	else:
		resp = make_response(jsonify({"msg":'User with same email id exists, Please Login.'}),202)
		resp.headers["Content-Type"] = "application/json"
		return resp

# Login
@app.route('/login',methods=['POST'])
def login():
	data = request.json
	User = Query()
	user = db.search(User["email"] == data["email"])
	if len(user) == 0:
		resp = make_response(
			jsonify({"msg":'No account'}),
			401,
			{'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'})
		resp.headers["Content-Type"] = "application/json"
		return resp
	else:
		if check_password_hash(user[0]["password"],data["password"]):
			token = jwt.encode({
				'id': user[0]["id"],
				'exp': datetime.utcnow() + timedelta(minutes = 30)
			}, app.config['JWT_SECRET_KEY'],algorithm="HS256")
			resp = make_response(jsonify({"msg": "Success", "user":user[0]["name"] ,"token": token}),201)
			resp.headers["Content-Type"] = "application/json"
			return resp
		else:
			resp = make_response(
			    jsonify({"msg":"Wrong password"}),
			    403,
			    {'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'}
			)
			resp.headers["Content-Type"] = "application/json"
			return resp

# Serve route
@app.route("/")
def home():
	return send_from_directory(app.static_folder,'index.html')

if __name__ == "__main__":
	# Prepare the labelencoder
	with open('dis_class.json','r') as file:
		dis_class = json.load(file)

	lb = preprocessing.LabelEncoder()
	lb.classes_ = np.asarray(dis_class)

	# Load Model in onnxruntime
	clf = load("./dis_pred.joblib")

	# Load local database
	db = TinyDB('user_database.json')

	# Run Flask app
	app.run()

