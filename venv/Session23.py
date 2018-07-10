from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(iris)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

print(iris.data)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(iris.target)


clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

lbl = clf.predict([[5.0,2.0,3.5,1.0]])

print(lbl)


import graphviz

dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("iris")

dot_data = tree.export_graphviz(clf, out_file=None,
                         feature_names=iris.feature_names,
                         class_names=iris.target_names,
                         filled=True, rounded=True,
                         special_characters=True)
graph = graphviz.Source(dot_data)
graph.view()