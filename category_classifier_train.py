import pandas as pd
import numpy as np
import nltk
import pickle
import csv
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import f1_score

stop_words = set(stopwords.words('english'))
def remove_stopwords(text):
    clean_text = [w for w in text.split() if not w in stop_words]
    return ' '.join(clean_text)

input_text, categories = [], []

with open("csmm_data.csv", 'r') as csmm_data_file:
    reader = csv.reader(csmm_data_file)
    for row in tqdm(reader):
        input_text.append(remove_stopwords(row[0]))
        categories.append(row[1].split('|'))

pickle.dump(categories, open('category_list.sav', 'wb'))

csmm_data = pd.DataFrame({ 'text': input_text, 'categories': categories })

category_tag = MultiLabelBinarizer()
category_tag.fit(csmm_data['categories'])
category = category_tag.transform(csmm_data['categories'])


tfidf_vectorizer = TfidfVectorizer(max_features = 10000)

text_train, train_values, category_train, category_values = train_test_split(csmm_data['text'], category, test_size = 0.2, random_state = 0)

text_train_tfidf = tfidf_vectorizer.fit_transform(text_train)
train_values_tfidf = tfidf_vectorizer.transform(train_values)

logistic_reg = LogisticRegression()

classifier = OneVsRestClassifier(logistic_reg)

classifier.fit(text_train_tfidf, category_train)

pickle.dump((classifier, category_tag, tfidf_vectorizer), open('category_classifier_model.sav', 'wb'))

