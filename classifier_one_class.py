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

out = open('resultados_classifier_one_class.csv', 'w')

tr = 'cenario5/unsupervised/positivos_FAVE.csv'
te = 'cenario5/unsupervised/positivos_negativos_FAVE.csv'
tr_dataset = pandas.read_csv(tr, header=None)
te_dataset = pandas.read_csv(te, header=None)

f = 12

if f == 0:
    out.write('FAVE\n')
if f == 12:
    out.write('MAVE\n')

for i in range(10):
    X = tr_dataset.values[:19800, f:24]

    outlier = te_dataset.values[19800:, f:24]
    Y = te_dataset.values[19800:, 24]

    print(len(X))
    print(len(Y))
    print(len(outlier))

    X = shuffle(X)
    outlier, Y = shuffle(outlier, Y)

    svm = OneClassSVM()
    isf = IsolationForest()

    svm.fit(X)
    isf.fit(X)

    prediction_svm = svm.predict(outlier)
    prediction_isf = isf.predict(outlier)

    for i in range(len(Y)):
        Y[i] = Y[i] * -1

    for i in range(len(prediction_svm)):
        prediction_svm[i] = prediction_svm[i] * -1

    for i in range(len(prediction_isf)):
        prediction_isf[i] = prediction_isf[i] * -1

    acc_svm = accuracy_score(Y, prediction_svm)
    p_svm = precision_score(Y, prediction_svm)
    r_svm = recall_score(Y, prediction_svm)
    f1_svm = f1_score(Y, prediction_svm)
    print('\nSVM:')
    print('accuracy:  {:5.4} %'.format(acc_svm * 100))
    print('precision: {:5.4} %'.format(p_svm * 100))
    print('recall:    {:5.4} %'.format(r_svm * 100))
    print('f-measure: {:5.4} %'.format(f1_svm * 100))
    out.write('SVM')
    out.write(';')
    out.write(str(acc_svm).replace('.', ','))
    out.write(';')
    out.write(str(p_svm).replace('.', ','))
    out.write(';')
    out.write(str(r_svm).replace('.', ','))
    out.write(';')
    out.write(str(f1_svm).replace('.', ','))
    out.write(';')


    acc_isf = accuracy_score(Y, prediction_isf)
    p_isf = precision_score(Y, prediction_isf)
    r_isf = recall_score(Y, prediction_isf)
    f1_isf = f1_score(Y, prediction_isf)
    print('\nISF')
    print('accuracy:  {:5.4} %'.format(acc_isf * 100))
    print('precision: {:5.4} %'.format(p_isf * 100))
    print('recall:    {:5.4} %'.format(r_isf * 100))
    print('f-measure: {:5.4} %'.format(f1_isf * 100))
    out.write('ISF')
    out.write(';')
    out.write(str(acc_isf).replace('.', ','))
    out.write(';')
    out.write(str(p_isf).replace('.', ','))
    out.write(';')
    out.write(str(r_isf).replace('.', ','))
    out.write(';')
    out.write(str(f1_isf).replace('.', ','))
    out.write(';')
    out.write('\n')

out.close()
