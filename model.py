from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.decomposition import TruncatedSVD
#giam so chieu du lieu 30000->300 
svd = TruncatedSVD(n_components=300, random_state=42)
svd.fit(X_data_tfidf)


X_data_tfidf_svd = svd.transform(X_data_tfidf)
X_test_tfidf_svd = svd.transform(X_test_tfidf)
def train_model(classifier, X_data, y_data, X_test, y_test, is_neuralnet=False, n_epochs=3):       
    X_train, X_val, y_train, y_val = train_test_split(X_data, y_data, test_size=0.1, random_state=42)
    
    if is_neuralnet:
        classifier.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=n_epochs, batch_size=512)
        
        val_predictions = classifier.predict(X_val)
        test_predictions = classifier.predict(X_test)
        val_predictions = val_predictions.argmax(axis=-1)
        test_predictions = test_predictions.argmax(axis=-1)
    else:
        classifier.fit(X_train, y_train)
    
        train_predictions = classifier.predict(X_train)
        val_predictions = classifier.predict(X_val)
        test_predictions = classifier.predict(X_test)
        
    print("Validation accuracy: ", metrics.accuracy_score(val_predictions, y_val))
    print("Test accuracy: ", metrics.accuracy_score(test_predictions, y_test))
    return classifier

clf = train_model(svm.SVC(), X_data_tfidf_svd, Y_train, X_test_tfidf_svd, Y_test, is_neuralnet=False)
pickle.dump(clf, open("/content/svm.pkl", 'wb'))
#inference
clf = pickle.load(open('/content/svm.pkl','rb'))
def preprocess(document):
  document = ' '.join(gensim.utils.simple_preprocess(document))
  document = word_tokenize(document, format="text")
  print(document)
  tfidf_vectorize = tfidf_vect.transform([document])
  svd_vect = svd.transform(tfidf_vectorize)
  return svd_vect
document = """
Thủ thành Manuel Neuer tự tin với khả năng ngược dòng của Bayern Munich khi đá lượt về tứ kết Champions League với PSG tối 13/4.

* PSG - Barca: 2h thứ Tư 14/4, giờ Hà Nội.

"Chúng tôi cần cái đầu lạnh và trái tim nóng. Trước những cầu thủ nhanh nhẹn của PSG, chúng tôi cần tiếp cận hợp lý, với thái độ thi đấu tích cực, ổn định và giàu động lực", Neuer nói trên trang Bundesliga. "Chúng tôi cần bình tĩnh, tấn công và gây áp lực cho PSG. Họ có những vấn đề ở hàng thủ. Nếu tạo được nhiều cơ hội như trận lượt đi, chúng tôi có thể ngược dòng".

Bayern dứt điểm 31 lần nhưng chỉ ghi được hai bàn vào lưới PSG ở lượt đi tứ kết trên sân Allianz hôm 7/4. Ảnh: LÉquipe
Bayern dứt điểm 31 lần nhưng chỉ ghi được hai bàn vào lưới PSG ở lượt đi tứ kết trên sân Allianz hôm 7/4. Ảnh: L'Équipe.

Lượt đi giữa tuần trước, Bayern thua PSG 2-3 ngay trên sân nhà Allianz Arena. Để vào bán kết, họ cần thắng cách biệt một bàn nhưng từ tỷ số 4-3 trở lên, hoặc cách biệt tối thiểu hai bàn trên sân Công viên các Hoàng tử. Tuy nhiên, Bayern vẫn vắng tiền đạo chủ lực Robert Lewandowski do chấn thương. Tiền đạo cánh Serge Gnabry cũng phải nghỉ trận thứ hai liên tiếp ở Champions League do chưa hết Covid-19.

Ngoài ra, theo cựu danh thủ Lothar Matthaus, đương kim vô địch Bayern còn gặp vấn đề trong cách vận hành lối chơi. Ông nhận xét: "Bayern luôn chấp nhận mạo hiểm, nhưng khi mất bóng, họ không còn chắc chắn như mùa trước. Họ cũng thiếu tốc độ và sự khôn khéo".

Trái lại, PSG chỉ có một mối bận tâm về nhân sự là chấn thương của Marquinhos. Trong trận thắng Strassbourg 4-1 tại Ligue I tuần trước, trung vệ thủ quân người Brazil phải ngồi ngoài.

Điểm mạnh của PSG là cặp tiền đạo Neymar - Kylian Mbappe. Ở lượt đi, Mbappe lập cú đúp, còn Neymar góp hai kiến tạo. Nếu duy trì được lợi thế trước Bayern, họ sẽ vào bán kết và gặp đội thắng trong cặp Dortmund - Man City. Ở lượt đi, Man City thắng 2-1 trên sân nhà Etihad.
 """
test = preprocess(document)
clf.predict(test)