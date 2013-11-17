import logging, gensim, bz2

def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    id2word = gensim.corpora.Dictionary.load('../Data/dicts/2012.dict')
    mm = gensim.corpora.MmCorpus('../Data/dicts/2012_tfidf.mm')

    lda = gensim.models.ldamodel.LdaModel(corpus = mm, id2word = id2word, 
            num_topics = 20, update_every = 0, passes = 20)

    lda.save('../Data/model/2012.lda')

    docs = [lda[doc] for doc in mm]

    index = gensim.similarities.MatrixSimilarity(docs)
    index.save('../Data/model/2012.index')

    for i in range(len(docs)):
        sims = index[docs[i]]

        sims = sorted(enumerate(sims), key=lambda item: -item[1])
        for doc in sims:
            if doc[0] == i:
                sims.remove(doc)
                break

        print 'For #', i, sims

    #topics = lda.show_topics(20)
    #for topic in topics:
        #print topic

if __name__ == "__main__":
    main()
