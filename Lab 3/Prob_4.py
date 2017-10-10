import nltk
from nltk import pos_tag,ne_chunk
from nltk.tokenize import word_tokenize,wordpunct_tokenize,sent_tokenize
from nltk.corpus import wordnet as wn
from nltk.stem import PorterStemmer,LancasterStemmer,SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag

# Reading in the text file
text = open('input.txt','r')
line = text.readline()
print(line)

# Applying lemmatization
words = word_tokenize(line)  # Word tokenizing for lemmatization
print(words)
lem_text = []

for i in words:
    lemmatizer = WordNetLemmatizer()
    lemmatized = lemmatizer.lemmatize(i.lower())
    lem_text.append(lemmatized)
    print(lemmatized)

# Using POS tagging to identify verbs
print(lem_text)
pos_tagged = pos_tag(lem_text)
print(pos_tagged)
punct = ['.',',']  # Punctuation tags
verbs = ['VB','VBD','VBG','VBN','VBP','VBZ']  # Verb tags

# Removing the verbs from the text
for (tag,words) in pos_tagged:
    print(tag,words)
    for i in verbs:
        if words==i:
            lem_text.remove(tag)
print(lem_text)

# Removing the punctuations from the text
for i in lem_text:
    for j in punct:
        if i==j:
            lem_text.remove(i)
print(lem_text)

# Calculating word frequency of remaining words
fdist1 = nltk.FreqDist(lem_text)
common_words = fdist1.most_common(5)
print(fdist1.most_common(5))

# Performing sentence tokenization
sentences = sent_tokenize(line)
print(sentences)

# Remaking sentence of our liking
new_sentences = []

for i in sentences:
    print(i)
    for j in word_tokenize(i):
        print(j)
        for (k,l) in common_words:
            if j==k:
                new_sentences.append(i)  # Creating sentences containing the most common words

print(new_sentences)