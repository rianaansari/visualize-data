#%%
from unicodedata import category
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
pd.set_option("max_rows", 600)
from pathlib import Path  
import glob
from data_cleaning import normalize
from itertools import count
import matplotlib.dates as mdates
import arabic_reshaper
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
import csv
from bidi.algorithm import get_display
from hazm import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import VarianceThreshold
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer


#%%
data = pd.read_csv(r'C:\Users\admin\Desktop\tg\diagram\normal_data.csv')
data = data.dropna().sample(frac=1).reset_index()
#%%
with open(r"C:\Users\admin\Desktop\tg\tag recomendation\stopwords.txt" , encoding="utf-8") as txt_file :
    stop_word = [word.strip()for word in txt_file.readlines()]
#%%
def remove_stops(txt):
    txt = normalize(txt)
    txt_list = word_tokenize(txt)
    clean_txt = [word for word in txt_list if word not in stop_word]
    return " ".join(clean_txt)

#%%
txt_clean = []
for txt in tqdm(data['txt']):
    removed_stops = remove_stops(txt)
    txt_clean.append(removed_stops)

# %%

data['clean_txt']=txt_clean
# %%
tfidf_vectorizer = TfidfVectorizer(max_features=1000)
doc_vec = tfidf_vectorizer.fit_transform(txt_clean)
tfidf_vectorizer.get_feature_names_out()
constant_filter = VarianceThreshold(threshold = 0.0002)
# print(doc_vec)
# doc_vec.shape

# %%
categoryes = data['label'][:40000]
count_vect = CountVectorizer(max_features=10000)
X_train_counts = count_vect.fit_transform(txt_clean[:40000])
X_train_counts.shape

# %%
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape
# %%
clf = MultinomialNB().fit(X_train_tfidf, categoryes)
# %%
X_new_counts = count_vect.transform(txt_clean[40000:])
X_new_tfidf = tfidf_transformer.transform(X_new_counts)
predicted = clf.predict(X_new_tfidf)
true_labels = data['label'][40000:].to_list()
i = 0
for doc, category in zip(txt_clean, predicted):
    print('%r => %s' % (doc, category))
    i += 1
    if i > 10:
        break

# %%
# print(true_labels)
# print(predicted)
# %%
c = 0

for i in range(len(predicted)):
    if predicted[i]== true_labels[i]:
        c += 1
print(c/len(predicted))

# %%
