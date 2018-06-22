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


tr = 'engine.csv'
te = 'outlier_titles.csv'
tr_dataset = pandas.read_csv(tr, header=None)
te_dataset = pandas.read_csv(te, header=None)

models = []

X = tr_dataset.values[:, 0:24]
Y = tr_dataset.values[:, 24]

X2 = te_dataset.values[:, 0:24]
Y2 = te_dataset.values[:, 24]

print(len(X))
print(len(X2))

X, Y = shuffle(X, Y)
X2, Y2 = shuffle(X2, Y2)

# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
# X2_train, X2_test, y2_train, y2_test = train_test_split(X2, Y2, test_size=0.9)

# g = GaussianNB()
# k= KMeans(n_clusters=1)
svm = OneClassSVM()
isf = IsolationForest()

# g.fit(X, Y)
# k.fit(X, Y)
svm.fit(X)
isf.fit(X)


# prediction_g = g.predict(X)
# prediction_k = k.predict(X2)
prediction_svm = svm.predict(X2)
prediction_isf = isf.predict(X2)

prediction_svm_train = svm.predict(X)
n_erros_svm = prediction_svm_train[prediction_svm_train == -1].size
print(n_erros_svm)

n_acertos_svm = prediction_svm[prediction_svm == -1].size
print(n_acertos_svm)
print(f'% de acertos: {n_acertos_svm/len(X2)}')


n_acertos_isf = prediction_isf[prediction_isf == -1].size
print(n_acertos_isf)
print(f'% de acertos: {n_acertos_isf/len(X2)}')
