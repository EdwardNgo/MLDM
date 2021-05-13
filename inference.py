import pickle
from underthesea import word_tokenize
X_train = pickle.load(open('preprocessed_data/Y_test.pkl','rb'))
print(X_train[0])