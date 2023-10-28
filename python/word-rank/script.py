# coding=utf-8

# input: array with multiple strings
# expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

import string
import re
sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2

translator = str.maketrans("", "", string.punctuation)
words = " ".join(sentences).lower().translate(translator).split(" ")
words_dict = {word: words.count(word) for word in set(words)}
top = sorted(words_dict.items(), key=lambda item: -item[1])
count = 1

for idx in range(len(top)):
    if count > 3:
        break
    print(f'{count}. "{top[idx][0]}" - {top[idx][1]}')
    if top[idx][1] != top[idx+1][1]:
        count += 1

# Good luck! You can write all the code in this file.
