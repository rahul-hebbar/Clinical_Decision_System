import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn import tree
import json
from joblib import dump

# Read the CSV
df = pd.read_csv("./datasets/HSD_net/CSV/clean.csv")

# Write the columns to a JSON
with open("symp.json","w") as file:
	temp_list = df.columns.to_list()[1:]
	symp_lis = [{"id": i,"text":val} for i,val in enumerate(temp_list)]
	json.dump(symp_lis,file)

# Label Binarize the Categorical Column (integer OneHotEncoding)
disease = df.pop("Disease Term")
lb = preprocessing.LabelEncoder()
X_label = lb.fit_transform(disease.values)

# Write the classes of Label Binrizer for future use
with open("dis_class.json","w") as f:
	json.dump(lb.classes_.tolist(),f)

# Train Decision Tree Model
clf = tree.DecisionTreeClassifier()
X_train = np.int64(df.values)
clf.fit(X_train,X_label)
print('Training finished')

# Convert model to joblib
dump(clf,'dis_pred.joblib')