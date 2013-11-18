import logging, gensim, bz2, pickle

def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    id2word = gensim.corpora.Dictionary.load('../Data/dicts/2012.dict')
    mm = gensim.corpora.MmCorpus('../Data/dicts/2012_tfidf.mm')

    lda = gensim.models.ldamodel.LdaModel(corpus = mm, id2word = id2word, 
            num_topics = 20, update_every = 0, passes = 20)
    lda.save('../Data/model/2012.lda')

    topics = lda.show_topics(20)

    pickle.dump(topics, open("../Data/model/topics.p", "wb"))

    #for topic in topics:
        #print topic

if __name__ == "__main__":
    main()
