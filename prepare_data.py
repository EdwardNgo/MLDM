import os
import glob
from tqdm import tqdm
import pickle
from underthesea import word_tokenize
import gensim
import re
train_dirs = glob.glob('Train_Full/*')
test_dirs = glob.glob('Test_Full/*')
stop_words = [word.replace(' ','_') for word in open('stopwords.txt','r').read().split('\n')]

def remove_stop_words(document):
    words = [word for word if word not in stop_words in document.split()]
    return ' '.join(words)

def preprocess(document):
    # tách từ
    document = word_tokenize(document, format="text")
    # đưa về lower
    document = document.lower()
    # xóa các ký tự không can thiết
    document = re.sub(r'[^\s\wáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ_]',' ',document)
    # xóa khoảng trắng thừa
    document = re.sub(r'\s+', ' ', document).strip()
    document = remove_stop_words(document)
    return document

def mergeTxtFile(dirs,final_dir):
    for directory in dirs:
        txt_files = glob.glob(directory+"/*")
        topic = directory.split('/')[-1].replace(' ','_')
        with open(final_dir+topic+".txt",'w') as f:
            for i in tqdm(range(len(txt_files))):
                with open(txt_files[i],'r',encoding='utf-16') as tf:
                    data = tf.read().replace('\n','')
                f.write(data+'\n')

def getNormalizedData(path):
    files = os.listdir(path)
    X = []
    Y = []
    for f in files:
        label = f.replace('.txt','')
        with open(path+'/' + f) as tf:
            data = tf.read().split('\n')[:-1]
            # data = [' '.join(gensim.utils.simple_preprocess(line)) for line in data]
            # data = [word_tokenize(line, format="text") for line in data]
            X = X + data
            Y = Y + [label]*len(data)
    return X,Y
X_test,Y_test = getNormalizedData('data/test')
print(len(X_test),len(Y_test))
X_train,Y_train = getNormalizedData('data/train')
print(len(X_train),len(Y_train))
# print(X_train[0])
# for i in [X_train,X_test,Y_train,Y_test]:
#     pickle.dump(i,open('data/' + i + '.pkl'))