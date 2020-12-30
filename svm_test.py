from libsvm.svmutil import *
from libsvm.svm import *

#y, x = svm_read_problem('lda_test_theme_distrib')
y, x = svm_read_problem('tfidf_test')

model = svm_load_model('svm_model')
p_labs, p_acc, p_vals = svm_predict(y, x, model)

print(p_acc)
