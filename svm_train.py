from libsvm.svmutil import *
from libsvm.svm import *

#y, x = svm_read_problem('lda_train_theme_distrib')
y, x = svm_read_problem('tfidf_train')
print("read ok")
model = svm_train(y, x, '-t 0 -c 10')

svm_save_model('svm_model', model)
