import numpy
from matplotlib import pyplot
from itertools import cycle
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import auc
from sklearn.metrics import average_precision_score
from sklearn import metrics
from scipy import interp
from sklearn.preprocessing import label_binarize


pyplot.figure()
pyplot.plot(,,label='SVM curve(area = {0:0.2f})' ''.format(roc_auc))
