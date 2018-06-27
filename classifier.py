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


# data = 'author_and_outlier.csv'
data = 'auto_tests/model_auto_outlier_cen4.csv'
dataset = pandas.read_csv(data, header=None)

models = []

X = dataset.values[:, 0:24]
Y = dataset.values[:, 24]

acum_acc_g = 0
acum_r_g = 0
acum_p_g = 0

acum_acc_knn = 0
acum_r_knn = 0
acum_p_knn = 0

for i in range(10):
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.999)
    print(len(X_train))

    g = GaussianNB()
    # k = KMeans(n_clusters=1)
    knn = KNeighborsClassifier()
    # svm = OneClassSVM()

    g.fit(X_train, y_train)
    # k.fit(X_train, y_train)
    knn.fit(X_train, y_train)
    # svm.fit(X)

    prediction_g = g.predict(X_test)
    # prediction_k = k.predict(X_test)
    prediction_knn = knn.predict(X_test)
    # prediction_svm = svm.predict(X)
    print('\nGaussianNB:')
    print('accuracy:  {:5.4} %'.format(accuracy_score(y_test, prediction_g) * 100))
    print('precision: {:5.4} %'.format(precision_score(y_test, prediction_g) * 100))
    print('recall:    {:5.4} %'.format(recall_score(y_test, prediction_g) * 100))

    print('\nKNN:')
    print('accuracy:  {:5.4} %'.format(accuracy_score(y_test, prediction_knn) * 100))
    print('precision: {:5.4} %'.format(precision_score(y_test, prediction_knn) * 100))
    print('recall:    {:5.4} %'.format(recall_score(y_test, prediction_knn) * 100))

    acum_acc_g += accuracy_score(y_test, prediction_g)
    acum_r_g += precision_score(y_test, prediction_g)
    acum_p_g += recall_score(y_test, prediction_g)

    acum_acc_knn += accuracy_score(y_test, prediction_knn)
    acum_r_knn += precision_score(y_test, prediction_knn)
    acum_p_knn += recall_score(y_test, prediction_knn)


print('\nMedias:')
print('GaussianNB:')
print('accuracy:  {:5.4} %'.format((acum_acc_g / 10) * 100))
print('precision: {:5.4} %'.format((acum_r_g / 10) * 100))
print('recall:    {:5.4} %'.format((acum_p_g / 10) * 100))

print('\nKNN:')
print('accuracy:  {:5.4} %'.format((acum_acc_knn / 10) * 100))
print('precision: {:5.4} %'.format((acum_p_knn / 10) * 100))
print('recall:    {:5.4} %'.format((acum_r_knn / 10) * 100))
