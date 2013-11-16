from gensim import corpora, models, similarities
from stemming.porter2 import stem
import string

def main():
    f = open('2012data.txt', 'r')
    url = f.readline()
    f.readline()
    doc = []
    table = string.maketrans("","")
    while True:
        line = f.readline().strip()
        s = line.translate(table, string.punctuation)
        s = " ".join([stem(word) for word in s.split(" ")])
        if line.startswith("</Content>"): break
        doc.append(s.lower())

    print doc

if __name__ == "__main__":
    main()
