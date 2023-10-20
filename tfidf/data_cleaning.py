
#%%
import re 
import emoji
import json
import itertools
from unicodedata import category
import pandas as pd 
from tqdm import tqdm
import os


#%%

alphabets_regex = {
                    'ا':r'اَ|اِ|اُ|اٌ|اٍ|اً|أ|إ',
                    'ب':r'بَ|بِ|بُ|بّ',
                    'پ':r'پَ|پِ|پُ',
                    'ت':r'تَ|تِ|تُ|تّ',
                    'ث':r'ثَ|ثِ|ثُ',
                    'ج':r'جَ|جِ|جُ|جّ',
                    'چ':r'چَ|چِ|چُ|چّ',
                    'ح':r'حَ|حِ|حُ',
                    'خ':r'خَ|خِ|خُ',
                    'د':r'دَ|دِ|دُ|دّ',
                    'ذ':r'ذَ|‌ذِ|ذُ',
                    'ر':r'رَ|رِ|رُ|رّ',
                    'ز':r'زَ|زِ|زُ|زّ',
                    'ژ':r'ژَ|ژِ|ژُ',
                    'س':r'سَ|سِ|سُ|سّ',
                    'ش':r'شَ|شِ|شُ',
                    'ص':r'صَ|صِ|صُ',
                    'ض':r'ضَ|ضِ|ضُ',
                    'ط':r'طَ|طِ|طُ',
                    'ظ':r'ظَ|ظِ|ظُ',
                    'ع':r'عَ|عِ|عُ',
                    'غ':r'غَ|غِ|غُ',
                    'ف':r'فَ|فِ|فُ|فّ',
                    'ق':r'قَ|قِ|قُ|قّ',
                    'ک':r'کَ|کِ|کُ|ك|كَ|كِ|كُ|کّ|كّ',
                    'گ':r'گَ|گِ|گُ',
                    'ل':r'لَ|لِ|لُ|لّ',
                    'م':r'مَ|مِ|مُ',
                    'ن':r'نَ|نِ|نُ|نّ',
                    'و':r'وَ|وِ|وُ|ؤ|ؤَ|ؤُ|ؤِ|وّ|ؤّ',
                    'ه':r'هَ|هِ|هُ|ة',
                    'ی':r'یَ|یِ|یُ|ي|يَ|يِ|يُ|يّ|یّ',
                    'ئ':r'ئَ|ئِ|ئُ|ئّ'
                    }

#%%

SYMBOLS = [
            '/', '?', '.',
            ',', '!', '@',
            '#', '$', '%',
            '*', '&', '^',
            '(', ')', '\\',
            '~', '`', "'",
            '|', '[', ']',
            '{', '}', ';',
            ':', '>', '<',
            '"', ';', '،',
            '؟', '-', '_']

#%%

PERSIAN_CHARACTER = [
            'الف', 'ب', 'پ',
            'ت', 'ث', 'ج',
            'چ', 'ح', 'خ',
            'د', 'ذ', 'ر',
            'ز', 'ژ', 'س',
            'ش', 'ص', 'ض',
            'ط', 'ظ', 'ع',
            'غ', 'ف', 'ق',
            'ک', 'گ', 'ل',
            'م', 'ن', 'و',
            'ه', 'ی', 'ء',
            'آ', 'اً', 'هٔ',
            'ا', 'ً', 'ٌ',
            'ٍ', 'َ', 'ُ',
            'ِ', 'ّ', 'ۀ',
            'ة', 'ي', 'ؤ',
            'إ', 'أ', 'ء'
        ]

eng_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',\
                     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
eng_pattern = r'(?:{})'.format('|'.join([r"{}".format(ch) for ch in eng_alphabets]))

#%%

def emoji_space(text):
    edited_text = ""
    for ch in text:
        if ch in emoji.UNICODE_EMOJI:
            edited_text = edited_text + " "+ch+" "
        else:
            edited_text = edited_text + ch
    return edited_text


       
#%%

def unifing_alphabets(text):
    text = re.sub(alphabets_regex['ا'], 'ا', text)
    text = re.sub(alphabets_regex['ب'], 'ب', text)
    text = re.sub(alphabets_regex['پ'], 'پ', text)
    text = re.sub(alphabets_regex['ت'], 'ت', text)
    text = re.sub(alphabets_regex['ث'], 'ث', text)
    text = re.sub(alphabets_regex['ج'], 'ج', text)
    text = re.sub(alphabets_regex['چ'], 'چ', text)
    text = re.sub(alphabets_regex['ح'], 'ح', text)
    text = re.sub(alphabets_regex['خ'], 'خ', text)
    text = re.sub(alphabets_regex['د'], 'د', text)
    text = re.sub(alphabets_regex['ذ'], 'ذ', text)
    text = re.sub(alphabets_regex['ر'], 'ر', text)
    text = re.sub(alphabets_regex['ز'], 'ز', text)
    text = re.sub(alphabets_regex['ژ'], 'ژ', text)
    text = re.sub(alphabets_regex['س'], 'س', text)
    text = re.sub(alphabets_regex['ش'], 'ش', text)
    text = re.sub(alphabets_regex['ص'], 'ص', text)
    text = re.sub(alphabets_regex['ض'], 'ض', text)
    text = re.sub(alphabets_regex['ط'], 'ط', text)
    text = re.sub(alphabets_regex['ظ'], 'ظ', text)
    text = re.sub(alphabets_regex['ع'], 'ع', text)
    text = re.sub(alphabets_regex['غ'], 'غ', text)
    text = re.sub(alphabets_regex['ف'], 'ف', text)
    text = re.sub(alphabets_regex['ق'], 'ق', text)
    text = re.sub(alphabets_regex['ک'], 'ک', text)
    text = re.sub(alphabets_regex['گ'], 'گ', text)
    text = re.sub(alphabets_regex['ل'], 'ل', text)
    text = re.sub(alphabets_regex['م'], 'م', text)
    text = re.sub(alphabets_regex['ن'], 'ن', text)
    text = re.sub(alphabets_regex['و'], 'و', text)
    text = re.sub(alphabets_regex['ه'], 'ه', text)
    text = re.sub(alphabets_regex['ی'], 'ی', text)
    text = re.sub(alphabets_regex['ئ'], 'ئ', text)
    return text



#%%

def editTitle(title):

    if title == '' or title is None:
        return ''
    title = title.strip()
    temp = title.split()
    temp_list = ['']
    new_title = []

    for word in temp:
        if word not in SYMBOLS:  # for ex title en = سلام _ خوبي ,  temp = ['سلام' , '_', 'خوبي']
            word = re.sub(r"(\w)\.", r'\1', word)  # for ex word word ==  س.ل.ا.م , then return
            for symbol in SYMBOLS:
                if symbol in word:
                    word = word.replace(symbol, '')  # for ex,  word ==  سلام_خوبي
        chars=''
        if word not in SYMBOLS:  # for ex title en = سلام _ خوبي ,  temp = ['سلام' , '_', 'خوبي']
            word = re.sub(r"(\w)\.", r'\1', word)  # for ex word word ==  س.ل.ا.م , then return
            word = re.sub(r'[^\w\d\s]+', '', word)
            word = ''.join(ch for ch in word if not category(ch).startswith('P'))
            for symbol in SYMBOLS:
                if symbol in word:
                    word = word.replace(symbol, '')  # for ex,  word ==  سلام_خوبي

            new_title.append(word)
    res = ''
    current_index = -1
    for word in new_title:
        word = word.strip()
        flag_blank = True
        for char in word:
            if char in PERSIAN_CHARACTER or char == " ":
                res += char
                current_index += 1
        res += " "
        current_index += 1
    res = res.strip()
    return res.lower()


#%%

def remove_extra_chars(text):
    text = text.lower()

    # if url exists in the text
    url_pattern = r"(?:(?:https?):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+"
    if re.findall(url_pattern, text, re.IGNORECASE):
        text = re.sub(url_pattern,"",text)

    # if username exists in the text
    if re.findall(r"@(\w+[.]*\b)", text):
        text = re.sub(r"@(\w+[.]*\b)","",text)

    # remove english characters
    text = re.sub(eng_pattern, '', text)

    # if number length is more than 3 numbers
    text = re.sub(r'\d{3,}', '', text)

    # if text contains extra character
    # remove all punctuation in fasttext or glove in ai_model
    regex = re.compile('[%s]' % re.escape('"#$&\'()*+-/<=>@[\\]^_`{|}~'))
    text = regex.sub(' ', text)

    # unifying all alphabets in the text
    text = unifing_alphabets(text)

    # if text contains duplicate letters
    duplicate_letter_pattern = re.compile(r"(.)\1{2,}")
    text_with_pattern2 = duplicate_letter_pattern.sub(r"\1\1", text)
    text = (" ").join([word.strip() for word in text_with_pattern2.split()])
    return text



#%%

def normalize (text):
    text = emoji_space(text)
    text = unifing_alphabets(text)
    text = editTitle(text)
    text = remove_extra_chars(text)
    return text
