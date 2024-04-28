import re
import string
from pymystem3 import Mystem

STOPWORDS = []
with open("data/stopwords.txt", "r") as file:
    # Читаем все строки файла, удаляем символы переноса и заносим их в массив lines
    STOPWORDS = [line.strip() for line in file]
    file.close()

PUNCTUATION = re.compile('[%s]' % re.escape(string.punctuation))
STEMMER = Mystem()


def tokenize(text):
    return text.split()


def lowercase_filter(tokens):
    return [token.lower() for token in tokens]


def punctuation_filter(tokens):
    return [PUNCTUATION.sub('', token) for token in tokens]

def stopword_filter(tokens):
    return [token for token in tokens if token not in STOPWORDS]


def stem_filter(tokens):
    return STEMMER.lemmatize(' '.join(tokens))


def analyze(text):
    tokens = tokenize(text)
    tokens = lowercase_filter(tokens)
    tokens = punctuation_filter(tokens)
    tokens = stopword_filter(tokens)
    tokens = stem_filter(tokens)

    return [token for token in tokens if token]
