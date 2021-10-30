from keras.models import Sequential
from keras.layers import Dense,Dropout
import numpy
from sklearn.preprocessing import MinMaxScaler
from numpy import array

numpy.random.seed(7)
classification = 2
dataset = numpy.loadtxt("new_set.csv" , delimiter=",")

X_samples = dataset[:,0:14]
Y_samples = dataset[:,14]

X = numpy.array(X_samples)
Y = numpy.array(Y_samples)
##y_train = keras.utils.to_categorical(y_train-1, classification)
##y_test = keras.utils.to_categorical(y_test-1, classification)

scaler = MinMaxScaler(feature_range=(0,1))
x_train = scaler.fit_transform((X))


#tanh=89, softmax, elu=88(0.7 test), selu, softplus, softsign=89(0.79), relu, sigmoid, hard_sigmoid=89(0.72), exponential, linear  
model = Sequential()
model.add(Dense(10, input_dim=14, activation='softsign'))
model.add(Dense(7, activation='softsign'))
model.add(Dense(5, activation='softsign'))
model.add(Dense(3, activation='tanh'))
model.add(Dense(1, activation='hard_sigmoid'))

model.compile(loss="mean_squared_error", optimizer="Nadam", metrics=['accuracy'])

model.fit(x_train,Y, epochs = 10, validation_split=0.1, batch_size = 100)


scores = model.evaluate(x_train,Y)
print("\n%s: %.2f%%" % (model.metrics_names[1],scores[1]*100))
##data1 = numpy.loadtxt("test_sample.csv" , delimiter=",")
##x = array([[-1,-1,-1,-1,-1,1,-1,-1,1,1,1,0,1,0,0,0,-1,1,1,1,0]])
###y = data1[:,21]
##predictions = model.predict(x)
#predictions = model.predict_classes(x)---> to round off
##print ("X=%s, Predicted=%s" % (x[0],predictions[0]))

