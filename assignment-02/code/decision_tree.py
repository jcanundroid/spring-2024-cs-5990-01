# -------------------------------------------------------------------------
# AUTHOR: Jeremy Anunwah
# FILENAME: decision_tree.py
# SPECIFICATION: calculate the performance of decision trees
# FOR: CS 5990 (Advanced Data Mining) - Assignment #2
# TIME SPENT: 40 minutes
# -----------------------------------------------------------*/

# importing some Python libraries

from sklearn import tree
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataSets = ['cheat_training_1.csv', 'cheat_training_2.csv']

def transformFeatures(i):
	return [
		1 if i[0] == 'Yes' else 0,
		1 if i[1] == 'Single' else 0,
		1 if i[1] == 'Divorced' else 0,
		1 if i[1] == 'Married' else 0,
		float(i[2][:-1])
	]

# read the test data and add this data to data_test NumPy

df = pd.read_csv('cheat_test.csv', sep = ',', header = 0)
df = np.array(df.values)[:, 1:]

data_test_classes = list(map(lambda x: 1 if x[3] == 'Yes' else 2, df))
data_test = list(map(transformFeatures, df))

for ds in dataSets:
	df = pd.read_csv(ds, sep = ',', header = 0) # reading a dataset eliminating the header (Pandas library)
	data_training = np.array(df.values)[:, 1:]  # creating a training matrix without the id (NumPy library)

	# transform the original training features to numbers and add them to the 5D array X. For instance, Refund = 1, Single = 1, Divorced = 0, Married = 0,
	# Taxable Income = 125, so X = [[1, 1, 0, 0, 125], [2, 0, 1, 0, 100], ...]]. The feature Marital Status must be one-hot-encoded and Taxable Income must
	# be converted to a float.

	x = list(map(transformFeatures, data_training))

	# transform the original training classes to numbers and add them to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]

	y = list(map(lambda x: 1 if x[3] == 'Yes' else 2, data_training))

	totalAccuracy = 0.0

	# loop your training and test tasks 10 times here

	for i in range (10):
		# fitting the decision tree to the data by using Gini index and no max_depth

		clf = tree.DecisionTreeClassifier(criterion = 'gini', max_depth = None)
		clf = clf.fit(x, y)

		# plotting the decision tree

		tree.plot_tree(clf, feature_names = ['Refund', 'Single', 'Divorced', 'Married', 'Taxable Income'], class_names = ['Yes', 'No'], filled = True, rounded = True)
		plt.show()

		correctPredictions = 0

		for i, data in enumerate(data_test):
			# transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:

			class_predicted = clf.predict([data])[0]

			# compare the prediction with the true label (located at data[3]) of the test instance to start calculating the model accuracy.

			if class_predicted == data_test_classes[i]:
				correctPredictions += 1

		# find the average accuracy of this model during the 10 runs (training and test set)

		totalAccuracy += correctPredictions / len(data_test)

	# print the accuracy of this model during the 10 runs (training and test set).
	# your output should be something like that: final accuracy when training on cheat_training_1.csv: 0.2

	print('final accuracy when training on {}: {}'.format(ds, totalAccuracy / 10.0))
