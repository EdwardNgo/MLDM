from flask import Flask, render_template,request,jsonify
import pickle
import os
import glob
from tqdm import tqdm
import pickle
from underthesea import word_tokenize
import gensim
from sklearn.decomposition import TruncatedSVD

MODEL = "model"
MODEL_PATH = "model/svm.pkl"
WORD_EMBEDDING = "model/tfidf.pkl"
DATA_TRANSFORM = "model/tfidfdata.pkl"
SVD = "model/svd_data.pkl"
clf = pickle.load(open(MODEL_PATH,"rb"))
tfidf_vect = pickle.load(open(WORD_EMBEDDING,"rb"))
tfidf_data = pickle.load(open(DATA_TRANSFORM,"rb"))
# svd = TruncatedSVD(n_components=300, random_state=42)
# svd.fit(tfidf_data)
svd = pickle.load(open(SVD,"rb"))

app = Flask(__name__)

def preprocess(document):
    document = ' '.join(gensim.utils.simple_preprocess(document))
    document = word_tokenize(document, format="text")
    print(document)
    tfidf_vectorize = tfidf_vect.transform([document])
    svd_vect = svd.transform(tfidf_vectorize)
    return svd_vect

def preprocess_nb(document):
    document = ' '.join(gensim.utils.simple_preprocess(document))
    document = word_tokenize(document, format="text")
    print(document)
    tfidf_vectorize = tfidf_vect.transform([document])
    return tfidf_vectorize

@app.route('/get-category',methods = ['GET'])
def text_classify():
    document = request.args.get('document')
    print(document)
    # print(clf.predict_proba(text))
    document_vect = preprocess(document)
    label = clf.predict(document_vect)

    return {"content":document,"label":str(label[0])}

@app.route('/classification',methods=["GET"])
def init():
    # fetch available trained models
    try:
        print("Hi")
        trained_models = os.listdir(MODEL)
        # trained_models = ["model/"+fname for fname in trained_models]
        response = jsonify(trained_model=tuple(trained_models))
        response.headers.add("Access-Control-Allow-Origin", "*")

        return response
    except:
        return "500"

@app.route('/classification/predict/<model>',methods=["POST"])
def handle_predict_request(model):
    clf = pickle.load(open("model/"+model,"rb"))
    requested_data = request.get_json()
    input = requested_data['input']
    # f = open(TEST_FILE_PATH, "w",encoding='utf-16-le')
    # f.write(input)
    # f.close()
    # pred = Predictor()
    if "nb.pkl" in model:
        input_vect = preprocess_nb(input)
    else:
        input_vect = preprocess(input)
    label = clf.predict(input_vect)
    try:
        return label[0]
    except:
        return "500"

if __name__ == '__main__':
#     test = """
#  """
#     print(preprocess(test))
#     res = clf.predict(preprocess(test))
#     print(res)

    app.run()
