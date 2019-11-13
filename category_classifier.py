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
from sklearn.metrics import f1_score, accuracy_score

stop_words = set(stopwords.words('english'))
classifier, category_tag, tfidf_vectorizer = pickle.load(open('category_classifier_model.sav', 'rb'))

categories_dump = pickle.load(open('category_list.sav', 'rb'))

class Category:
    def __init__(self, name, confidence):
        self.name = name
        self.confidence = confidence

def remove_stopwords(text):
    clean_text = [w for w in text.split() if not w in stop_words]
    return ' '.join(clean_text)

def classify(input_text):
    input_text = remove_stopwords(input_text)

    input_text_tfidf = tfidf_vectorizer.transform([input_text])

    predict_categories = classifier.predict(input_text_tfidf)

    classified_categories = category_tag.inverse_transform(predict_categories)
    confidence = np.max(classifier.predict_proba(input_text_tfidf))

    result = [ Category(category, confidence) for category in list(classified_categories[0]) ]

    return result
r = classify('this is amazing soft skills')
