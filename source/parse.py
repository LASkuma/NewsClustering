from gensim import corpora, models, similarities
from stemming.porter2 import stem
import string
import re

def main():
    # Open utility and data files
    dataFile = open('../data/2012data.txt', 'r')
    stopFile = open('../data/english.stop.txt', 'r')

    # Read in stop list
    stopList = [line.strip() for line in stopFile]
    stopFile.close()

    # Parse in and remove punctuation
    doc = []                    # List to store the content of a single document
    url = dataFile.readline()   # Read the first line as url
    dataFile.readline()         # Skip the <Content> tag
    while True:
        line = dataFile.readline().strip()
        if line.startswith("</Content>"): break
        s = " ".join(re.split('\W+', line.lower()))
        doc.append(s)
       
    # Remove stop words
    texts = [[word for word in document.lower().split() if word not in stopList]
             for document in doc]

    # Remove words that only appear once
    # all_tokens = sum(texts, [])
    # tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
    # texts = [[word for word in text if word not in tokens_once]
    #          for text in texts]

    # Stemming
    result = [" ".join([stem(word) for word in line]) for line in texts]

    print result

if __name__ == "__main__":
    main()
