import pandas as pd  
import numpy
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.ensemble import AdaBoostClassifier
from sklearn import metrics
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix

dataset = numpy.loadtxt("Finaldataset.csv" , delimiter=",")
X = dataset[:,0:16]
Y = dataset[:,16]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2,random_state=5)

################ SVM
clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Accuracy by SVM:",metrics.accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
roc = roc_auc_score(y_test,y_pred)
print('ROC for SVM: %.3f' % roc)

##########   Random Forest
clf1=RandomForestClassifier(n_estimators=100)
clf1.fit(X_train,y_train)
y_pred1=clf1.predict(X_test)
print("Accuracy by RF:",metrics.accuracy_score(y_test, y_pred1))
print(confusion_matrix(y_test, y_pred1))
roc = roc_auc_score(y_test,y_pred1)
print('ROC for RF: %.3f' % roc)

############## Naive Bayes
model = GaussianNB()
model.fit(X_train,y_train)
predicted= model.predict(X_test)
print("Accuracy by NB:",metrics.accuracy_score(y_test, predicted))
print(confusion_matrix(y_test, predicted))
roc = roc_auc_score(y_test,predicted)
print('ROC for RF: %.3f' % roc)


############### Logistic Regression
logreg = LogisticRegression()
logreg.fit(X_train,y_train)
y_pred2=logreg.predict(X_test)
print("Accuracy by LR:",metrics.accuracy_score(y_test, y_pred2))
print(confusion_matrix(y_test, y_pred2))
roc = roc_auc_score(y_test,y_pred2)
print('ROC for RF: %.3f' % roc)


################ Adaboost
abc = AdaBoostClassifier(n_estimators=50,
                         learning_rate=1)
model = abc.fit(X_train, y_train)
y_pred3 = model.predict(X_test)
print("Accuracy by Adaboost:",metrics.accuracy_score(y_test, y_pred3))
print(confusion_matrix(y_test, y_pred3))
roc = roc_auc_score(y_test,y_pred3)
print('ROC for RF: %.3f' % roc)

