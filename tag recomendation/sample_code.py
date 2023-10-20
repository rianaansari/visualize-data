#%%
import pandas as pd
from tqdm import tqdm
from data_cleaning import normalize
from wordcloud_fa import WordCloudFa
import arabic_reshaper
from hazm import *
from bidi.algorithm import get_display
import arabic_reshaper


# %%
data = pd.read_csv(r'C:\Users\admin\Desktop\tg\tag recomendation\normal_data.csv')
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
wordcloud = WordCloudFa(persian_normalize=True)
wordcloud = WordCloudFa(include_numbers=False)
wordcloud = WordCloudFa(no_reshape=True)
wordcloud = WordCloudFa(collocations=False)

#%%
txt_clean = []
for txt in tqdm(data['txt']):
    removed_stops = remove_stops(txt)
    txt_clean.append(removed_stops)

# %%
data['clean_txt']=txt_clean
# %%
geography = list(data.loc[data['label']=="Geography", 'clean_txt'])
art = list(data.loc[data['label']=="Art", 'clean_txt'])
english = list(data.loc[data['label']== "English",'clean_txt' ])
physic = list(data.loc[data['label']=="Physic", 'clean_txt'])
ct = list(data.loc[data['label']=="Computers and Technology", 'clean_txt'])
health = list(data.loc[data['label']=="Health", 'clean_txt'])
history = list(data.loc[data['label']=="History", 'clean_txt'])
chemistry = list(data.loc[data['label']=="chemistry", 'clean_txt'])
biology = list(data.loc[data['label']=="Biology", 'clean_txt'])
mathematics = list(data.loc[data['label']=="mathematics", 'clean_txt'])
cooking = list(data.loc[data['label']=="cooking", 'clean_txt'])
game = list(data.loc[data['label']=="game", 'clean_txt'])
foreign_language = list(data.loc[data['label']=="foreign language", 'clean_txt'])
philosophy = list(data.loc[data['label']=="philosofy", 'clean_txt'])
psychology = list(data.loc[data['label']=="psycology", 'clean_txt'])
travel = list(data.loc[data['label']=="travel", 'clean_txt'])
life_style = list(data.loc[data['label']=="life style", 'clean_txt'])
environment = list(data.loc[data['label']=="environment", 'clean_txt'])
business = list(data.loc[data['label']=="business", 'clean_txt'])
architecture = list(data.loc[data['label']=="architecture", 'clean_txt'])
social_studies = list(data.loc[data['label']=="social studies", 'clean_txt'])
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
    text = list_category[get_display(arabic_reshaper.reshape(item))]
    for txt in text:
        label_txt = " "
        label_txt += " " + txt
    wc = wordcloud.generate(label_txt)
    image = wc.to_image()
    image.show()
    image.save(f'wordcloud_{item}.png')
