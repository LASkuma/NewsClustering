import logging, gensim, bz2

def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    id2word = gensim.corpora.Dictionary.load('../Data/dicts/2012.dict')
    mm = gensim.corpora.MmCorpus('../Data/dicts/2012_tfidf.mm')

    lda = gensim.models.ldamodel.LdaModel(corpus = mm, id2word = id2word, 
            num_topics = 20, update_every = 0, passes = 20)

    lda.save('../Data/model/2012.lda')

    #docs = [lda[doc] for doc in mm]

    #for doc in docs:
        #print doc

    #topics = lda.show_topics(20)
    #for topic in topics:
        #print topic

if __name__ == "__main__":
    main()
