#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    5
"""
from __future__ import division
import pickle
import sys
sys.path.append('D:/Machine Learning/final_project/')
from poi_email_addresses import poiEmails
sys.path.append('D:/Machine Learning/tools/')
from feature_format import featureFormat,targetFeatureSplit

enron_data = pickle.load(open("D:/Machine Learning/final_project/final_project_dataset.pkl", "r"))


payed = []
pois = []

for person in enron_data:        # Second Example
    if(enron_data[person]["poi"]==1):
        pois.append(person)
        if(enron_data[person]["total_payments"]=='NaN'):
            payed.append(person)

percentage = (len(payed)+10)/(len(enron_data)+10)*100
print((len(payed)+10))
print(len(pois)+10)
