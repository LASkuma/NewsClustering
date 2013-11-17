from gensim import corpora, models, similarities
def main():
    dictionary = corpora.Dictionary.load('../Data/dicts/2012.dict')
    corpus = corpora.MmCorpus('../Data/dicts/2012.mm')
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    corpora.MmCorpus.serialize('../Data/dicts/2012_tfidf.mm', corpus_tfidf)
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=20)
    corpus_lsi = lsi[corpus_tfidf]
    lsi.save('../Data/dicts/2012_tfidf_transformation.lsi')
    print corpus
if __name__ == "__main__":
    main()