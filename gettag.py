import unicodedata
import string
import re
import random

class Tag:
    def __init__(self, term):
            self.term = term
            self.word2index = {}
            self.word2count = {}
            self.n_words = 2

    def addSentence(self, sentence):
        for word in sentence.split(' '):
            self.addWord(word)

    def addWord(self, word):
        if word not in self.word2index:
            self.word2index[word] = self.n_words
            self.word2count[word] = 1
        else:
            self.word2count[word] += 1

def unicodeToAscii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
    )

# Lowercase, trim, and remove non-letter characters
def normalizeString(s):
    s = unicodeToAscii(s.lower().strip())
    s = re.sub(r"([.!?])", r" \1", s)
    s = re.sub(r"[^a-zA-Z.!?]+", r" ", s)
    return s

def readLangs(lang1='tag', lang2='category',reverse=False):
    print("Reading lines...")

    # Read the file and split into lines
    lines = open('data/tag.txt', encoding='utf-8').\
        read().strip().split('\n')

    # Split every line into pairs and normalize
    pairs = [[normalizeString(s) for s in l.split('100')] for l in lines]
    print(pairs)
    # Reverse pairs, make Lang instances
    if reverse:
        pairs = [list(reversed(p)) for p in pairs]
        tag = Tag(lang1)
        category = Tag(lang2)
    else:
        tag = Tag(lang1)
        category = Tag(lang2)

    return tag, category, pairs

def filterPairs(pairs):
    return [pair for pair in pairs]

def prepareData(lang1='tag', lang2='category', reverse=False):
    input_lang, output_lang, pairs = readLangs(lang1, lang2, reverse)
    print("Read %s sentence pairs" % len(pairs))
    pairs = filterPairs(pairs)
    print("Trimmed to %s sentence pairs" % len(pairs))
    print("Counting words...")
    for pair in pairs:
        print(pair[0])
        print(pair[1])
        input_lang.addSentence(pair[0])
        output_lang.addSentence(pair[1])
    print("Counted words:")
    print(input_lang.term, input_lang.n_words)
    print(output_lang.term, output_lang.n_words)
    return input_lang, output_lang, pairs

input_lang, output_lang, pairs = prepareData(True)
print(random.choice(pairs))
