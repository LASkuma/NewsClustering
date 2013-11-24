import gensim, pickle, logging, string
from stemming.porter2 import stem

def main():
    docs = pickle.load(open("../Data/dicts/2012docs.p", "rb"))
    topics = pickle.load(open("../Data/model/topics.p", "rb"))
    Table = pickle.load(open("../Data/dicts/HashTable.p", "rb"))
    dataFile = open('../Data/2012data.txt', 'r')
    wordPercent = {}
    sumSentence = []
    for i in range(len(topics)):
        # print topics[i]
        tmp = topics[i].split(' + ')
        for j in range(len(tmp)):
            wordlist = tmp[j].split('*')
            wordPercent[wordlist[1]] = wordlist[0]
    while True:
        trash = dataFile.readline()
        trash = dataFile.readline()
        doc = ""
        while True:
            line = dataFile.readline().strip()
            if line.startswith("</Content>"):
                sentences = doc.split('.')
                maxValue = 0
                maxIndex = 0
                for sentence in sentences:
                    words = sentence.split(' ')
                    sumPercent = 0
                    for word in words:
                        if stem(word) in wordPercent.keys():
                            sumPercent += float(wordPercent[stem(word)])
                        if sumPercent>maxValue:
                            maxValue = sumPercent
                            maxIndex = sentences.index(sentence)
                sumSentence.append(sentences[maxIndex])
                break
            doc += line
        if not dataFile.readline(): break
    print len(sumSentence)
    # for i in docs:
    #     print len(i)
    # print wordPercent
if __name__ == "__main__":
    main()