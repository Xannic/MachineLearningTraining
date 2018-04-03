#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("D:/Machine Learning/tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("D:/Machine Learning/final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]

data_dict.pop( "TOTAL")

data = featureFormat(data_dict, features)

maxSal = ("",0)

for person in data_dict:
    if(data_dict[person]["salary"]>maxSal[1] and data_dict[person]["salary"] != "NaN"):
        maxSal = (person,data_dict[person]["salary"])

print(maxSal)
### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


