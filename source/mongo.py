from pymongo import MongoClient
import pickle
#{id;title();content;url;sim();summa}
#{topicid;words;}
def main():
    # client = MongoClient('mongodb://root:nmlyodxfkpse@162.243.140.77:3002/127.0.0.1')
    client = MongoClient('162.243.140.77', 27017)
    urlList = pickle.load(open("../Data/dicts/urlList.p", "rb"))
    sim = pickle.load(open("../Data/model/sim_index.p", "rb"))
    t = pickle.load(open("../Data/model/topics.p", "rb"))
    Summ = pickle.load(open("../Data/model/Summarization.p", "rb"))
    title = pickle.load(open("../Data/dicts/title.p", "rb"))
    wordlist = pickle.load(open("../Data/dicts/topicwords.p", "rb"))
    cluster = pickle.load(open("../Data/model/cluster_index.p", "rb"))
    db = client.meteor
    collection = db.documents
    collection2 = db.topics
    docid = 1
    topicid = 1
    # print len(sim[1])
    # doc = {'id':docid, 'title':title[1], 'url':urlList[1], 'sim':[sim[1][i][0] for i in range(10)], 'summa':1}
    # print docid
    for i in range(len(t)):
        top = {'id':topicid, 'words':wordlist[i], 'docs':[cluster[i][j][0] for j in range(len(cluster[i]))]}
        topicid += 1
        collection2.insert(top)
    for sentence in Summ:
        doc = {'id':docid, 'title':title[Summ.index(sentence)], 'url':urlList[Summ.index(sentence)], 'sim':[sim[Summ.index(sentence)][i][0] for i in range(10)], 'summa':sentence}
        collection.insert(doc)
        docid += 1
    # collection.find_one({"something":"fortesting"})
    # tmpdoc = {"name":"Mike", "age":"19"}
    # collection.insert(tmpdoc)
if __name__ == "__main__":
    main()