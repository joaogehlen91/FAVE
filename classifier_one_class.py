# Load libraries

import pandas
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest
from sklearn.utils import shuffle
from sklearn.svm import OneClassSVM


tr = 'auto_tests/model_auto.csv'
te = 'auto_tests/model_auto_outlier_cen4-1.csv'
tr_dataset = pandas.read_csv(tr, header=None)
te_dataset = pandas.read_csv(te, header=None)

models = []

X = tr_dataset.values[:17743, 0:24]
# Y = tr_dataset.values[:, 24]

# X2 = tr_dataset.values[5000:5258, 0:24]

outlier = te_dataset.values[17743:, 0:24]
Y = te_dataset.values[17743:, 24]

print(len(X))
# print(len(X2))
print(len(outlier))

# X, Y = shuffle(X, Y)


X = shuffle(X)
outlier, Y = shuffle(outlier, Y)

# X2 = shuffle(X2)
# outlier = shuffle(outlier)

# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
# X2_train, X2_test, y2_train, y2_test = train_test_split(X2, Y2, test_size=0.9)

# g = GaussianNB()
k= KMeans(n_clusters=2)
svm = OneClassSVM()
isf = IsolationForest()

# g.fit(X, Y)
# k.fit(X, Y)
svm.fit(X)
isf.fit(X)
k.fit(X)


# prediction_g = g.predict(X)
# prediction_k = k.predict(X2)
prediction_svm = svm.predict(outlier)
prediction_isf = isf.predict(outlier)

# print(f'% de acertos K: {n_acertos_k_train/len(outlier)}')

print('accuracy:  {:5.4} %'.format(accuracy_score(Y, prediction_svm) * 100))
print('precision: {:5.4} %'.format(precision_score(Y, prediction_svm) * 100))
print('recall:    {:5.4} %'.format(recall_score(Y, prediction_svm) * 100))

print('accuracy:  {:5.4} %'.format(accuracy_score(Y, prediction_isf) * 100))
print('precision: {:5.4} %'.format(precision_score(Y, prediction_isf) * 100))
print('recall:    {:5.4} %'.format(recall_score(Y, prediction_isf) * 100))

# n_acertos_svm = prediction_svm[prediction_svm == -1].size
# print(n_acertos_svm)
# # print(f'% de acertos SVM: {n_acertos_svm_train/len(outlier)}')
#
# n_acertos_svm = prediction_svm[prediction_svm == 1].size
# print(n_acertos_svm)
# print(f'% de erros SVM: {n_acertos_svm_train/len(outlier)}')


# n_acertos_isf_outlier = prediction_isf_outlier[prediction_isf_outlier == -1].size
# print(n_acertos_isf_outlier)
# print(f'% de acertos SVM: {n_acertos_isf_outlier/len(outlier)}')


# n_acertos_isf = prediction_isf[prediction_isf == -1].size
# print(n_acertos_isf)
# print(f'% de acertos IF: {n_acertos_isf/len(outlier)}')
