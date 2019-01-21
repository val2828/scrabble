import urllib.request as ur
import re
import requests

url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
ur.urlretrieve(url, filename='all_words.txt')

with open('all_words.txt') as f:
    all_words = f.read()

all_words_ls = all_words.split()
pattern = r'[sndla][sndla][sndla]x$'
found = []
for word in all_words_ls:
    if re.search(pattern, word) is not None and len(word) <= 7:
        found.append(word)


print(found)
