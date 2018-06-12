# Load libraries

import pandas
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score


url = "out.csv"
dataset = pandas.read_csv(url, header=None)

models = []

X = dataset.values[:, 0:21]
Y = dataset.values[:, 21]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=21)

models.append(KNeighborsClassifier(n_neighbors=15))
# models.append(svm.SVC())
models.append(GaussianNB())
models.append(KMeans(n_clusters=2, random_state=21))


for model in models:
    model.fit(X_train, y_train)


for model in models:
    prediction = model.predict(X_test)
    print('')
    print(model.__class__.__name__)
    print('accuracy:  {:5.4} %'.format(accuracy_score(y_test, prediction) * 100))
    # print('recall:    {:5.4} %'.format(recall_score(y_test, prediction) * 100))
    # print('precision: {:5.4} %'.format(precision_score(y_test, prediction) * 100))
    # print('f1:        {:5.4} %'.format(f1_score(y_test, prediction) * 100))
