# -------------------------------------------------------------------------
# AUTHOR: Jeremy Anunwah
# FILENAME: roc_curve.py
# SPECIFICATION: Compute the ROC curve for a decision tree classifier
# FOR: CS 5990 (Advanced Data Mining) - Assignment #2
# TIME SPENT: 40 minutes
# -----------------------------------------------------------*/

# importing some Python libraries

from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from matplotlib import pyplot
import numpy as np
import pandas as pd

# read the dataset cheat_data.csv and prepare the data_training numpy array

data_training = np.loadtxt('cheat_data.csv', delimiter = ',', dtype = 'str')[1:]

# transform the original training features to numbers and add them to the 5D array X. For instance, Refund = 1, Single = 1, Divorced = 0, Married = 0,
# Taxable Income = 125, so X = [[1, 1, 0, 0, 125], [0, 0, 1, 0, 100], ...]]. The feature Marital Status must be one-hot-encoded and Taxable Income must
# be converted to a float.

def transformFeatures(i):
	return [
		1 if i[0] == 'Yes' else 0,
		1 if i[1] == 'Single' else 0,
		1 if i[1] == 'Divorced' else 0,
		1 if i[1] == 'Married' else 0,
		float(i[2][:-1])
	]

x = list(map(transformFeatures, data_training))

# transform the original training classes to numbers and add them to the vector y. For instance Yes = 1, No = 0, so Y = [1, 1, 0, 0, ...]

y = list(map(lambda x: 1 if x[3] == 'Yes' else 0, data_training))

# split into train/test sets using 30% for test

trainX, testX, trainY, testY = train_test_split(x, y, test_size = 0.30)

# generate a no skill prediction (random classifier - scores should be all zero)

ns_probs = np.zeros(len(testX))

# fit a decision tree model by using entropy with max depth = 2

clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth = 2)
clf = clf.fit(trainX, trainY)

# predict probabilities for all test samples (scores)

dt_probs = clf.predict_proba(testX)

# keep probabilities for the positive outcome only

dt_probs = list(map(lambda x: x[1], dt_probs))

# calculate scores by using both classifiers (no skilled and decision tree)

ns_auc = roc_auc_score(testY, ns_probs)
dt_auc = roc_auc_score(testY, dt_probs)

# summarize scores

print('No Skill: ROC AUC = %.3f' % (ns_auc))
print('Decision Tree: ROC AUC = %.3f' % (dt_auc))

# calculate roc curves

ns_fpr, ns_tpr, _ = roc_curve(testY, ns_probs)
dt_fpr, dt_tpr, _ = roc_curve(testY, dt_probs)

# plot the roc curve for the model

pyplot.plot(ns_fpr, ns_tpr, linestyle = '--', label = 'No Skill')
pyplot.plot(dt_fpr, dt_tpr, marker = '.', label = 'Decision Tree')

# axis labels

pyplot.xlabel('False Positive Rate')
pyplot.ylabel('True Positive Rate')

# show the legend

pyplot.legend()

# show the plot

pyplot.show()
