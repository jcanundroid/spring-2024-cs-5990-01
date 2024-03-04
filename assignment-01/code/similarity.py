# -------------------------------------------------------------------------
# AUTHOR: Jeremy Anunwah
# FILENAME: similarity.py
# SPECIFICATION: output the two most similar documents according to their
#                cosine similarity
# FOR: CS 5990 (Advanced Data Mining) - Assignment #1
# TIME SPENT: 30 minutes
# -----------------------------------------------------------*/

# Importing some Python libraries

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Defining the documents

doc1 = "soccer is my favorite sport"
doc2 = "I like sports and my favorite one is soccer"
doc3 = "support soccer at the olympic games"
doc4 = "I do like soccer, my favorite sport in the olympic games"

# Use the following words as terms to create your document-term matrix
# [soccer, favorite, sport, like, one, support, olympic, games]

matrix = []
words = ['soccer', 'favorite', 'sport', 'like', 'one', 'support', 'olympic', 'games']
docs = [doc1, doc2, doc3, doc4]

for doc in docs:
	docVector = []
	docWords = doc.split(' ')

	for word in words:
		n = 0

		for docWord in docWords:
			if docWord == word:
				n += 1

		docVector.append(n)

	matrix.append(docVector)

# Compare the pairwise cosine similarities and store the highest one
# Use cosine_similarity([X], [Y]) to calculate the similarities between 2 vectors only
# Use cosine_similarity([X, Y, Z]) to calculate the pairwise similarities between multiple vectors

pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

maxPairS = 0
maxPairSIndex = 0

for i, pair in enumerate(pairs):
	s = cosine_similarity([matrix[pair[0]]], [matrix[pair[1]]])[0][0]

	if s > maxPairS:
		maxPairS = s
		maxPairSIndex = i

maxMultiS = cosine_similarity(matrix)

maxPair = pairs[maxPairSIndex]

# Print the highest cosine similarity following the information below
# The most similar documents are: doc1 and doc2 with cosine similarity = x

print('The most similar documents are: doc{} and doc{} with cosine similarity = {}'.format(
	maxPair[0] + 1, maxPair[1] + 1, maxPairS
))
