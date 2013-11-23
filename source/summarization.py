import gensim, pickle, logging, string

def main():
    docs = pickle.load(open("../Data/model/doc_index.p", "rb"))
    topics = pickle.load(open("../Data/model/topics.p", "rb"))
    Table = pickle.load(open("../Data/dicts/HashTable.p", "rb"))
    wordlist = []
    for i in range(len(topics)):
        # print topics[i]
        tmp = topics[i].split(' + ')
        tmplist = []
        for j in range(len(tmp)):
            tmplist.append(tmp[j].split('*'))
        wordlist.append(tmplist)
    # for i in docs:
    #     print len(i)
    print wordlist
if __name__ == "__main__":
    main()