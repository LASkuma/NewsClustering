#NewsClustering#

This is a repo for CS473 Final Project. It's aimed to cluster news threads from [Purdue Newsroom](http://www.purdue.edu/newsroom/) and give summarizations for each thread.

#Getting Started#
1. Install [Python](http://www.python.org) (3.0 > Python >= 2.5)
2. Install dependencies for [gensim](http://radimrehurek.com/gensim/index.html), including [NumPy](http://sourceforge.net/projects/numpy/files/) and [SciPy](http://sourceforge.net/projects/scipy/files/). 
3. Install [gensim](http://radimrehurek.com/gensim/index.html)
4. Install [stemming 1.0](https://pypi.python.org/pypi/stemming/1.0) You can install with `easy_install -U stemming` if easy_install is installed

You can find detailed [Install Steps](http://radimrehurek.com/gensim/install.html) from gensim website .

#To-do#
1. ~~Save document urls~~
2. ~~Transform to sparse~~
3. ~~LDA step~~
4. ~~Inverse hash stemmed word to original word~~
5. ~~Do TF-IDF tranform to corpus~~
6. ~~Similarity queries for all the documents (Clustering)~~
7. Summarize topics
8. Evaluation [Datasets for single-label text categorization](http://web.ist.utl.pt/~acardoso/datasets/)

#Data#
The file "2012data.txt" in Data directory is used as the input for this project. It has the following structure

__url__\n

__\<Content>__\n

__title__\n

__content__\n

__\<\Content>__\n

\n

#Doc_index#
doc[doc_b] is a list of pairs. Each pair is (topic_id, probability).


#Resources#
[Python Official Tutorial](http://docs.python.org/2/tutorial/index.html)
