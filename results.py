from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import auc
from sklearn.metrics import average_precision_score
from matplotlib import pyplot
import numpy
import keras
from numpy import array
import pandas as pd
from sklearn import metrics

numpy.random.seed(7)

dataset = numpy.loadtxt("Finaldataset.csv" , delimiter=",")

X = dataset[:,0:16]
y = dataset[:,16]

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=5)


model = Sequential()
model.add(Dense(12, input_dim=16, activation='relu'))
model.add(Dense(15, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['accuracy'])
model.fit(X_train,y_train, epochs = 10, batch_size = 30, validation_data=(X_test,y_test))

y_pred = model.predict_classes(X_test)
#print(metrics.accuracy_score(y_test,y_pred))
#print(confusion_matrix(y_test, y_pred))
#y_pred = y_pred[:,1]
roc = roc_auc_score(y_test,y_pred)
print('AUC: %.3f' % roc)

fpr,tpr, thresholds = roc_curve(y_test, y_pred)

pyplot.plot([0,1], [0,1], linestyle='--')
pyplot.plot(fpr, tpr, marker='.')
pyplot.show()

precision, recall, thresholds = precision_recall_curve(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc = auc(recall, precision)
ap = average_precision_score(y_test, y_pred)
print('f1=%.3f auc=%.3f ap=%.3f' % (f1, auc, ap))
pyplot.plot([0,1], [0.5,0.5], linestyle='--')
pyplot.plot(recall, precision, marker='.')
pyplot.show()
