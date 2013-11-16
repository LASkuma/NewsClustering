from gensim import corpora, models, similarities
from stemming.porter2 import stem
import string

def main():
    f = open('2012data.txt', 'r')
    stop = open('english.stop.txt', 'r')
    stoplist = []
    url = f.readline()
    f.readline()
    doc = []
    result = []
    table = string.maketrans("","")
    while True:
        line = f.readline().strip()
        if line.startswith("</Content>"): break
        doc.append(line)
    for lines in stop:
        stoplist.append(lines.strip())
    texts = [[word for word in document.lower().split() if word not in stoplist]
             for document in doc]
    # all_tokens = sum(texts, [])
    # tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
    # texts = [[word for word in text if word not in tokens_once]
    #          for text in texts]
    for line in texts:
        line = str(line)
        s = line.translate(table, string.punctuation)
        s = " ".join([stem(word) for word in s.split(" ")])
        result.append(s.lower())
    print result

if __name__ == "__main__":
    main()
