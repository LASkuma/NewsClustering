from gensim import corpora, models, similarities
from stemming.porter2 import stem
import string
import re
import logging
import pickle

def main():
    # Open utility and data files
    dataFile = open('../Data/2012data.txt', 'r')
    stopFile = open('../Data/english.stop.txt', 'r')
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    # Read in stop list
    stopList = [line.strip() for line in stopFile]
    stopFile.close()

    # Parse in and remove punctuation
    docs = []                       # List to store the contents of all the documents
    urlList = []                    # List stores all the urls in the documents
    while True:
        strContent = ""             # String to store content of a single document
        url = dataFile.readline()   # Read the first line as url
        urlList.append(url)
        dataFile.readline()         # Skip the <Content> tag
        while True:
            line = dataFile.readline().strip()
            if line.startswith("</Content>"): break
            s = " ".join(re.split('\W+', line.lower()))
            strContent += ' ' + s

        docs.append(strContent)
        if not dataFile.readline(): break
    pickle.dump(urlList, open("../Data/dicts/urlList.p", "wb"))
    dataFile.close()
    # Remove stop words
    texts = [[word for word in document.lower().split() if word not in stopList]
             for document in docs]

    # Stemming
    result = [[stem(word) for word in line] for line in texts]

    # Inverse stemming
    Table  = {}
    for line in texts:
        for word in line:
            Table[stem(word)] = word
    pickle.dump( Table, open( "../Data/dicts/HashTable.p", "wb" ) )

    # Remove words that only appear once
    all_tokens = sum(result, [])
    tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
    texts = [[word for word in text if word not in tokens_once]
            for text in result]

    dictionary = corpora.Dictionary(texts)
    dictionary.save('../Data/dicts/2012.dict')

    print dictionary

    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize('../Data/dicts/2012.mm', corpus)

    print corpus

if __name__ == "__main__":
    main()
