# Load libraries

import pandas
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, \
    f1_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

buying_map = {'vhigh': 0, 'high': 1, 'med': 2, 'low': 3}
maint_map = {'vhigh': 0, 'high': 1, 'med': 2, 'low': 3}
doors_map = {'2': 2, '3': 3, '4': 4, '5more': 5}
persons_map = {'2': 2, '4': 4, 'more': 5}
lug_boot_map = {'small': 0, 'med': 1, 'big': 2}
safety_map = {'low': 0, 'med': 1, 'high': 2}
class_map = {'title': 1.0, 'outlier': 0.0}

url = "databases/car_evaluation.csv"
names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
n = len(names) - 1
dataset = pandas.read_csv(url, names=names)


dataset['buying'] = dataset['buying'].map(buying_map)
dataset['maint'] = dataset['maint'].map(maint_map)
dataset['doors'] = dataset['doors'].map(doors_map)
dataset['persons'] = dataset['persons'].map(persons_map)
dataset['lug_boot'] = dataset['lug_boot'].map(lug_boot_map)
dataset['safety'] = dataset['safety'].map(safety_map)
dataset['class'] = dataset['class'].map(class_map)

models = []

X = dataset.values[:, :n]
Y = dataset.values[:, n]

X_train, X_test, Y_train, y_test = train_test_split(X, Y, test_size=0.3,
                                                    random_state=100)

models.append(KNeighborsClassifier(n_neighbors=6))
models.append(svm.SVC(decision_function_shape='ovo'))
models.append(GaussianNB())


for model in models:
    model.fit(X_train, Y_train)


for model in models:
    prediction = model.predict(X_test)
    average = 'macro'

    print('')
    print(model.__class__.__name__)
    print('accuracy:  {:5.4} %'.format(accuracy_score(y_test, prediction) * 100))
    print('recall:    {:5.4} %'.format(recall_score(y_test, prediction, average=average) * 100))
    print('precision: {:5.4} %'.format(precision_score(y_test, prediction, average=average) * 100))
    print('f1:        {:5.4} %'.format(f1_score(y_test, prediction, average=average) * 100))
