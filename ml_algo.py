 from sklearn.datasets import load_iris
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split


from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import SGDClassifier


from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
accuracy_data = []


iris = load_iris()
print(iris['feature_names'])
# print(iris['data'])
#print('shape of data  : {}'.format(iris['data'].shape))
#print(iris['data'][-5:])
# print(iris['target'])
#a = iris['species'].value_count()
# drop_data = iris.drop('petal width (cm)',axis=1,inplace=True)
# print("drop data set petal width : ",drop_data)

x = iris['data']
y = iris['target']

X,Y = shuffle(x,y, random_state=0)
#print(X,Y)
X_train, x_test, Y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42)
#print(X_train, x_test, Y_train, y_test )
# print('x train :',X_train.shape)
# print('x test : ',x_test.shape)
# print('y train : ',Y_train.shape)
# print('y test : ',y_test.shape)


# 1 - DecisionTreeClassifier

classifier_dtree = DecisionTreeClassifier()
cls_dec = classifier_dtree.fit(X_train,Y_train)
predict = classifier_dtree.predict(x_test)
acc_Dtree = accuracy_score(y_test, predict, normalize=True)
accuracy_data.append(acc_Dtree)
print(accuracy_data)

#
#
# from sklearn.tree import export_graphviz
# from sklearn.externals.six import StringIO
# import pydot
# 0
# #features = list(iris.columns[1:])
# #print('features set : ',features)
# dot_data = StringIO()
# export_graphviz(classifier_dtree ,
#                 out_file=dot_data,
#                 feature_names=iris.feature_names,
#                 class_names=iris.target_names,
#                 filled=True,
#                 rounded=True,
#                 proportion=True
#                 )
# graph = pydot.graph_from_dot_data(dot_data.getvalue())
# graph[0].write_pdf('probability.pdf')
# print("graph : ",graph)
# probs = classifier_dtree.predict_proba(x_test)
# print("probability : ",probs)


#
# # 2 - RandomForestClassifier
#
# cls_rf = RandomForestClassifier()
# c = cls_rf.fit(X_train,Y_train)
# prediction_rf = cls_rf.predict(x_test)
# acc_rf = accuracy_score(y_test, prediction_rf, normalize=True)
# accuracy_data.append(acc_rf)
#
#
# # 3 - SVM (support vector machine)
#
# svm = SVC()
# S = svm.fit(X_train,Y_train)
# pre_svm = svm.predict(x_test)
# acc_svm = accuracy_score(y_test, pre_svm, normalize=True)
# accuracy_data.append(acc_svm)
#
# # 4 - K-Nearest Neighbours
#
# kn_cls = KNeighborsClassifier()
# knn = kn_cls.fit(X_train,Y_train)
# pre_kn = kn_cls.predict(x_test)
# acc_kn =accuracy_score(y_test, pre_kn, normalize=True)
# accuracy_data.append(acc_kn)




# # 5 -  Stochastic Gradient Descent
#
# sg_cls = SGDClassifier()
# sgd = sg_cls.fit(X_train,Y_train)
# pre_sg = sg_cls.predict(x_test)
# acc_sg = accuracy_score(y_test, pre_sg, normalize=True)
# accuracy_data.append(acc_sg)
#
# print("list data : ",accuracy_data)
#
# algor_name = ['DTC']
#
# plt.bar(algor_name,accuracy_data,label='first',color='r')
# plt.yticks(np.arange(0,1.1,0.1))
#
# plt.show()
# plt.close()

# Tree Visualization

# from sklearn.tree import export_graphviz
# from sklearn.externals.six import StringIO
# import pydot

#features = list(iris.columns[1:])
#print('features set : ',features)


"diffrent b/w numpay and pandas " \
"numpy data type is array a" \
"pandas is data frame like csv , txt etc file is data frame " \
"different b/w classifier and non classifier " \
"what is classifier " \
"what is regression " \
"different b/w supervise and unsupervise " \
"different b/w claasification and regretion " \
"what is data "

