import csv

with open("./datasets/147978_SDR.txt","r") as f:
	sdr = f.read()

with open("./datasets/322_S.txt","r") as f:
	s = f.read()

with open("./datasets/4442_D.txt","r") as f:
	d = f.read()

sdr_clean = [x.split("\t") for x in sdr.split("\n")]
s_clean = [x.split("\t") for x in s.split("\n")]
d_clean = [x.split("\t") for x in d.split("\n")]

print(sdr_clean[:10])
print(s_clean[:10])
print(d_clean[:10])

with open("./datasets/CSV/sym_dis_rel.csv","w",newline='') as fil:
	csv_writer = csv.writer(fil,delimiter = ",")
	csv_writer.writerows(sdr_clean)

with open("./datasets/CSV/sym.csv","w",newline='') as fil:
	csv_writer = csv.writer(fil,delimiter = ",")
	csv_writer.writerows(s_clean)

with open("./datasets/CSV/dis.csv","w",newline='') as fil:
	csv_writer = csv.writer(fil,delimiter = ",")
	csv_writer.writerows(d_clean)