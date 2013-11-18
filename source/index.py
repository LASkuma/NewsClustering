import logging, gensim, bz2, pickle

def main():
    mm = gensim.corpora.MmCorpus('../Data/dicts/2012_tfidf.mm')
    lda = gensim.models.ldamodel.LdaModel.load('../Data/model/2012.lda')

    docs = [lda[doc] for doc in mm]

    pickle.dump(docs, open("../Data/model/doc_index.p", "wb"))

    index = gensim.similarities.MatrixSimilarity(docs)
    index.save('../Data/model/2012.index')

    sims = []
    for i in range(len(docs)):
        sim = index[docs[i]]

        sim = sorted(enumerate(sim), key=lambda item: -item[1])
        for doc in sim:
            if doc[0] == i:
                sim.remove(doc)
                break
        sims.append(sim)

        #print 'For #', i, sim

    pickle.dump(sims, open("../Data/model/sim_index.p", "wb"))

    topics = {}
    for i in range(20):
        topics[i] = []

    for i in range(len(docs)):
        for topic in docs[i]:
            t = i, topic[1]
            topics[topic[0]].append(t)

    for num, topic in topics.iteritems():
        topics[num] = sorted(topic, key=lambda item: -item[1])

    pickle.dump(topics, open("../Data/model/cluster_index.p", "wb"))
    #print topics

if __name__ == "__main__":
    main()
