from pymongo import MongoClient
import pickle
#{id;title();content;url;sim();summa}
def main():
    client = MongoClient('localhost', 3002)
    urlList = pickle.load(open("../Data/dicts/urlList.p", "rb"))
    sim = pickle.load(open("../Data/model/sim_index.p", "rb"))
    Summ = pickle.load(open("../Data/model/Summarization.p", "rb"))
    title = pickle.load(open("../Data/dicts/title.p", "rb"))
    db = client.meteor                                                    # meteor: name of the database
    collection = db.documents                                             # documents: name of the collection
    docid = 1;
    # print len(sim[1])
    # doc = {'id':docid, 'title':title[1], 'url':urlList[1], 'sim':[sim[1][i][0] for i in range(10)], 'summa':1}
    # print docid
    for sentence in Summ:
        doc = {'id':docid, 'title':title[Summ.index(sentence)], 'url':urlList[Summ.index(sentence)], 'sim':[sim[Summ.index(sentence)][i][0] for i range(10)], 'summa':sentence}
        collection.insert(doc)
        docid += 1
    # collection.find_one({"something":"fortesting"})
    # tmpdoc = {"name":"Mike", "age":"19"}
    # collection.insert(tmpdoc)
if __name__ == "__main__":
    main()