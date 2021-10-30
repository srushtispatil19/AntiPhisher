from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import numpy
from numpy import array

numpy.random.seed(7)

dataset = numpy.loadtxt("Finaldataset.csv" , delimiter=",")

X = dataset[:,0:16]
Y = dataset[:,16]
#tanh=89, softmax, elu=88(0.7 test), selu, softplus, softsign=89(0.79), relu, sigmoid, hard_sigmoid=89(0.72), exponential, linear  
model = Sequential()
model.add(Dense(12, input_dim=16, activation='relu'))
model.add(Dense(15, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
## mean_squared_error
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['accuracy'])

model.fit(X,Y, epochs = 10, batch_size = 30)


scores = model.evaluate(X,Y)
print("\n%s: %.2f%%" % (model.metrics_names[1],scores[1]*100))
data1 = numpy.loadtxt("test_sample.csv" , delimiter=",")
test_sample = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,1,1]
x = array([test_sample])
#########y = data1[:,21]
predictions = model.predict(x)
##predictions = model.predict_classes(x)##### to round off
print ("X=%s, Predicted=%s" % (x[0],predictions[0]))
if(predictions[0] <= 0.5):
    print("LEGITIMATE")
else:
    print("PHISHY")

############### Save model

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
model.save_weights("model.h5")
print("Saved model to disk")

json_file = open('model.json','r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")
print("Loaded model from disk")
##
##loaded_model.compile(loss='binary_crossentropy', optimizer="adam", metrics=['accuracy'])
##score = loaded_model.evaluate(X,Y)
##print("\n%s: %.2f%%" % (loaded_model.metrics_names[1],score[1]*100))
##
x1 = array([[-1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,0,-1,1,1]])
prediction = loaded_model.predict(x1)
print ("X=%s, Predicted=%s" % (x1[0],prediction[0]))
