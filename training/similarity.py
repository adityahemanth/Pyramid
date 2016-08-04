from gensim import corpora, models, similarities
from hierarchy import tree
import os, sys

CORPUS_PATH = 'resources/master_corpus.svmlight'
DICT_PATH = 'resources/master_dict.dict'
INDEX_PATH = 'resources/master_index.index'
DOC_PATH = 'hierarchy/corpus'
TREE_PATH = 'resources/lcc.json'

class search:

	def __init__(self, corpus_path = CORPUS_PATH, dict_path = DICT_PATH):

		self.dictionary = corpora.Dictionary.load(dict_path)
		corpus = corpora.SvmLightCorpus(corpus_path)

		tfidf = models.TfidfModel(corpus)
		corpus_tfidf = tfidf[corpus]

		self.lsi = models.LsiModel(corpus_tfidf, id2word=self.dictionary, num_topics=2)
		self.tree = tree(TREE_PATH)


		try :
			self.index = similarities.MatrixSimilarity.load(INDEX_PATH)

		except:
			self.index = similarities.MatrixSimilarity(self.lsi[self.corpus])
			self.index.save(INDEX_PATH)
			print self.index


	def search(self, query):

		vec_bow = self.dictionary.doc2bow(query.lower().split())
		vec_lsi = self.lsi[vec_bow]
		sims = self.index[vec_lsi]
		sims = sorted(enumerate(sims), key=lambda item: -item[1] )

		index = sims[0][0]
		
		files = os.listdir(DOC_PATH)
		LCCN = files[index]
		LCCN = LCCN.split('.')
		LCCN = LCCN[0]

		return self.tree.getNode(LCCN)

