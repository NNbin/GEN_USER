from mimesis import Person
import nltk
from nltk.corpus import words
from random import choice
from transliterate import translit
import time

import requests
from bs4 import BeautifulSoup as bs


def check_username_availability(username):
    try:
        url = f"https://fragment.com/?query={username}"
        response = requests.get(url)
        soup = bs(response.text, "html.parser")
        status0 = soup.find('tbody', class_='tm-high-cells')
        status1 = status0.find('tr')
        status2 = status1.find_all('div')
        if status2[-1].text == 'Unavailable':
            status = True
        if status:
            return True
    except:
        return False
    

def name(lang):
    person = Person(lang)
    s = True
    while s:
        if lang == 'ru':
            n_ru = person.first_name()
            n_en = translit(n_ru, language_code='ru', reversed=True)
        elif lang == 'en':
            n_en = person.first_name()
        n_en = n_en.replace("'", '')
        if len(n_en) >= 6:
            if check_username_availability(n_en):
                s = False
                print(n_en)
                print(f'@{n_en.lower()}')
                print()


def word(lang):
    time.sleep(1)
    s = True
    while s:
        nltk.download('words')
        if lang == 'ru':
            words_f = words.words('ru')
            filtered_words = [word for word in words_f if len(word) > 5]
            word = choice(filtered_words)
            print(word)
            word = translit(word, language_code='ru', reversed=True)
            word = word.replace("'", '')
            if len(word) <= 5:
                break
        elif lang == 'en':
            words_f = words.words('en')
            filtered_words = [word for word in words_f if len(word) > 5]
            word = choice(filtered_words)
        if check_username_availability(word):
            s = False
            print(word)
            print(f'@{word.lower()}')
            print()


def main():
    categ = '0'
    lang = ''
    r = '0'
    print('''
  .g8"""bgd  `7MM"""YMM  `7MN.   `7MF'           `7MMF'   `7MF' .M"""bgd `7MM"""YMM  `7MM"""Mq.  
.dP'     `M    MM    `7    MMN.    M               MM       M  ,MI    "Y   MM    `7    MM   `MM. 
dM'       `    MM   d      M YMb   M               MM       M  `MMb.       MM   d      MM   ,M9  
MM             MMmmMM      M  `MN. M               MM       M    `YMMNq.   MMmmMM      MMmmdM9   
MM.    `7MMF'  MM   Y  ,   M   `MM.M               MM       M  .     `MM   MM   Y  ,   MM  YM.   
`Mb.     MM    MM     ,M   M     YMM               YM.     ,M  Mb     dM   MM     ,M   MM   `Mb. 
  `"bmmmdPY  .JMMmmmmMMM .JML.    YM                `bmmmmd"'  P"Ybmmd"  .JMMmmmmMMM .JMML. .JMM.
''')
    while categ not in ['1', '2']:
        categ = input('''
Категории:
1. Обычные слова (чаще сущ)
2. Имена
Выберите категорию: ''')
    while lang not in ['ru', 'en']:
        lang = input('Выберите язык(ru/en): ')
    while r not in ['1', '2']:
        r = input('''
Режимы:
1.Одиночный
2.Циклический
Выберите режим: ''')
    if r == '1':
        if categ == '1':
            word(lang)
        elif categ == '2':
            name(lang)
    elif r == '2':
        if categ == '1':
            while True:
                word(lang)
        elif categ == '2':
            while True:
                name(lang)


main()