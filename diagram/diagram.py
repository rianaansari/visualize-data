#%%
import arabic_reshaper
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
from bidi.algorithm import get_display
from hazm import *
from data_cleaning import normalize

# %%
data = pd.read_csv(r'C:\Users\admin\Desktop\tg\diagram\normal_data.csv')
data = data.dropna()

# %%
with open(r"C:\Users\admin\Desktop\tg\tag recomendation\stopwords.txt" , encoding="utf-8") as txt_file :
    stop_word = [word.strip()for word in txt_file.readlines()]
    
#%%
def remove_stops(txt):
    txt = normalize(txt)
    txt_list = word_tokenize(txt)
    clean_txt = [word for word in txt_list if word not in stop_word]
    return " ".join(clean_txt)

#%%
def str_words(label):
    word_list= []
    for i in label:
        n = i.split()
        word_list += n
    return word_list

#%%
def word_count(List):
    counts = dict()
    for item in List :
        
        if item in counts :
            counts[item]+= 1
        else:
            counts[item] = 1
    return counts

#%%
def sort_dic(dic):
    sorted_dic = list(sorted(dic.items(), key=lambda item: item[1]))
    return sorted_dic[-20: ]

#%%
txt_clean = []
for txt in tqdm(data['txt']):
    removed_stops = remove_stops(txt)
    txt_clean.append(removed_stops)

# %%
data['clean_txt']=txt_clean  
     
#%%
geography = data.loc[data['label']=="Geography", 'clean_txt'].to_list()
art = data.loc[data['label']=="Art", 'clean_txt'].to_list()
english = data.loc[data['label']== "English",'clean_txt' ].to_list()
physic = data.loc[data['label']=="Physic", 'clean_txt'].to_list()
ct = data.loc[data['label']=="Computers and Technology", 'clean_txt'].to_list()
health = data.loc[data['label']=="Health", 'clean_txt'].to_list()
history = data.loc[data['label']=="History", 'clean_txt'].to_list()
chemistry = data.loc[data['label']=="chemistry", 'clean_txt'].to_list()
biology = data.loc[data['label']=="Biology", 'clean_txt'].to_list()
mathematics = data.loc[data['label']=="mathematics", 'clean_txt'].to_list()
cooking = data.loc[data['label']=="cooking", 'clean_txt'].to_list()
game = data.loc[data['label']=="game", 'clean_txt'].to_list()
foreign_language = data.loc[data['label']=="foreign language", 'clean_txt'].to_list()
philosophy = data.loc[data['label']=="philosofy", 'clean_txt'].to_list()
psychology = data.loc[data['label']=="psycology", 'clean_txt'].to_list()
travel = data.loc[data['label']=="travel", 'clean_txt'].to_list()
life_style = data.loc[data['label']=="life style", 'clean_txt'].to_list()
environment = data.loc[data['label']=="environment", 'clean_txt'].to_list()
business = data.loc[data['label']=="business", 'clean_txt'].to_list()
architecture = data.loc[data['label']=="architecture", 'clean_txt'].to_list()
social_studies = data.loc[data['label']=="social studies", 'clean_txt'].to_list()

list_category={"Geography":geography,
               "Art":art,
               "English":english,
               "Physic":physic,
               "Computers and Technology":ct,
               "Health":health,
               "History":history,
               "chemistry":chemistry,
               "Biology":biology,
               "mathematics":mathematics,
               "cooking":cooking,
               "game":game,
               "foreign language":foreign_language,
               "philosofy":philosophy,
               "psycology":psychology,
               "travel":travel,
               "life style":life_style,
               "environment":environment,
               "business":business,
               "architecture":architecture,
               "social studies":social_studies,
}
#%%
for item in list_category :
    text = list_category[item]
    x = []
    y = []
    
    sortedwords = sort_dic(word_count(str_words(text)))
    
    
    for row in sortedwords:
        x.append(get_display(arabic_reshaper.reshape(row[0])))
        y.append(int(row[1]))
        
    fig, ax = plt.subplots(figsize=(5, 5), tight_layout=True)    
    plt.bar(x, y, color = 'g', width = 0.72, label = get_display(arabic_reshaper.reshape("تعداد")))
    
   
    plt.xlabel(get_display(arabic_reshaper.reshape('کلمات')))
    plt.ylabel(get_display(arabic_reshaper.reshape('شمارش')))
    plt.title(get_display(arabic_reshaper.reshape('بیش ترین 20 کلمه')))
    plt.legend()
    ax.tick_params(axis='x', rotation=70)
    plt.savefig(f"output_{item}.jpg")
    plt.show()
    
    
    
    
    
    
    











# %%
