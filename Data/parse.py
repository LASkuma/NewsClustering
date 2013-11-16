from gensim import corpora, models, similarities
from stemming.porter2 import stem
import string
import re

def main():
    f = open('2012data.txt', 'r')
    stop = open('english.stop.txt', 'r')
    stoplist = []
    url = f.readline()
    f.readline()
    doc = []
    table = string.maketrans("","")

    # Parse in and remove punctuation
    while True:
        line = f.readline().strip()
        if line.startswith("</Content>"): break
        s = " ".join(re.split('\W+', line.lower()))
        doc.append(s)
        
    # Read in stop list
    for lines in stop:
        stoplist.append(lines.strip())

    # Remove stop words
    texts = [[word for word in document.lower().split() if word not in stoplist]
             for document in doc]

    # all_tokens = sum(texts, [])
    # tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
    # texts = [[word for word in text if word not in tokens_once]
    #          for text in texts]

    # Stemming Step
    result = []
    for line in texts:
        s = " ".join([stem(word) for word in line])
        result.append(s)
    print result

if __name__ == "__main__":
    main()
