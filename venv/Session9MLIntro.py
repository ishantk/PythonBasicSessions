from sklearn import tree

"""
	Intro to Machine Learning

		Learning !!
		To Learn -> We need a Supervisor/Trainer


		Supervised Learing
			We need to provide data to machine

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


			Do it with ML Algo
			DecisionTree

			numpy
			scipy
			scikit-learn

"""

data = [[100,70],[120,90],[150,100],[800,1000],[1000,1100],[1200,1200]]
output = [0, 0, 0, 1, 1, 1]

clf = tree.DecisionTreeClassifier()
clf.fit(data,output)

#lbl = clf.predict([[110,85]])
lbl = clf.predict([[1000,100]])

print("Prediction is",lbl)
#print(type(lbl))

