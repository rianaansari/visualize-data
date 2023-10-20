#%%
from unicodedata import category
import pandas as pd
pd.set_option("max_rows", 600)
from data_cleaning import normalize
import pandas as pd
from tqdm import tqdm
from hazm import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import VarianceThreshold
from sklearn.naive_bayes import MultinomialNB

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

#%%
tfidf_vectorizer = TfidfVectorizer(max_features=10000)
X_train_tfidf = tfidf_vectorizer.fit_transform(txt_clean[:40000])
tfidf_vectorizer.get_feature_names_out()
constant_filter = VarianceThreshold(threshold = 0.0002)

#%%
categoryes = data['label'][:40000]

# %%
clf = MultinomialNB().fit(X_train_tfidf, categoryes)

# %%
X_new_counts = tfidf_vectorizer.transform(txt_clean[40000:])
predicted = clf.predict(X_new_counts)
true_labels = data['label'][40000:].to_list()
i = 0
for doc, category in zip(txt_clean, predicted):
    print('%r => %s' % (doc, category))
    i += 1
    if i > 10:
        break

# %%
c = 0
for i in range(len(predicted)):
    if predicted[i]== true_labels[i]:
        c += 1
print(c/len(predicted))