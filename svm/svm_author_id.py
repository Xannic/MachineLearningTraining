#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("D:/Machine Learning/tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

from sklearn import svm
from sklearn.metrics import accuracy_score

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

# for x in range(0, 20):
#     temp = x * 10 + 5200
#     clf = svm.SVC(kernel="rbf", C=temp)
#     t0 = time()
#     clf.fit(features_train,labels_train)
#     t1 = time()
#     pre = clf.predict(features_test)
#     clf.score(features_test,labels_test)
#     acc = accuracy_score(pre,labels_test)
#     if acc>highestAcc:
#         highestAcc= acc
#         c = temp
#         print('c:',temp)
#         print('acc:', acc)

# print('highest:', highestAcc)
# print('highest:', c)

clf = svm.SVC(kernel="rbf", C=10000)
t0 = time()
clf.fit(features_train,labels_train)
print('Fit time:', round(time()-t0,3))
t1 = time()
pred = clf.predict(features_test)
print('Predict time:', round(time()-t1,3))
clf.score(features_test,labels_test)
acc = accuracy_score(pred,labels_test)
print('Accuracy:', acc)

chrisCount = 0;
for x in pred:
    if(x==1):
        chrisCount+=1
print(chrisCount)
