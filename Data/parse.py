from gensim import corpora, models, similarities
from stemming.porter2 import stem
import string

def main():
    f = open('2012data.txt', 'r')
    url = f.readline()
    f.readline()
    doc = []
    while True:
        line = f.readline().strip()
        #line = line.translate(string.maketrans("",""), string.punctuation)
        if line.startswith("</Content>"): break
        doc.append(line)

    doc = [[stem(word) for word in sentence.split(" ")] for sentence in doc]

    doc = [" ".join(sentence) for sentence in doc]

    print doc

if __name__ == "__main__":
    main()
