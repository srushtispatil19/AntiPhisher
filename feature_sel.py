from sklearn.feature_selection import RFE
from sklearn.svm import SVR
import numpy
dataset = numpy.loadtxt("dataset.csv" , delimiter=",")
X = dataset[:,0:30]
Y = dataset[:,30]
#X,y = dataset(n_samples=15027, n_features=10, random_state=0)
estimator = SVR(kernel="linear")
selector = RFE(estimator, 15, step=1)
selector = selector.fit(X, Y)
print("before")
print(selector.support_)
selector.ranking_
print("after")
