"""

			Classification

			engine		weight		Vehicle
			X   		Y 			Z
			100cc       70kgs		bike 0
			120cc       90kgs		bike 0
			150cc       100kgs		bike 0

			800cc 		1000kgs     car 1
			1000cc 		1100kgs     car 1
			1200cc 		1200kgs     car 1


			110 cc + 85 kgs   =  ?

"""

from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB

import numpy as np

X = np.array([[100,70], [120,90], [150,100], [800,1000], [1000,1100], [1200,1200]])
Y = np.array([0, 0, 0, 1, 1, 1])

# model = GaussianNB()
# model = BernoulliNB()

model = MultinomialNB()
model.fit(X,Y)


lbl = model.predict([[110,85]])
print("Predicted Label ",lbl)

from sklearn.metrics import accuracy_score

Y_PRED = [0, 2, 1, 3]
Y_ORIG = [0, 1, 2, 3]

accScore = accuracy_score(Y_ORIG, Y_PRED)
print("Accuracy Score",accScore)