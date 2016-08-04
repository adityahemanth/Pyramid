'''
DESC.  :  Extracts keywords from 
'''

import os, sys
import json
from gensim import corpora
from collections import defaultdict

RESOURCE_PATH = 'resources/'
CORPUS_PATH = 'hierarchy/corpus/'
DICT_SAVE_PATH = 'resources/master_dict.dict'
CORPUS_SAVE_PATH = 'resources/master_corpus.svmlight'

class digester:

	def __init__(self):
		self.documents = []


	def digest(self):

		# creating a dictionary
		files = os.listdir(CORPUS_PATH)
		texts = []
		for file in files:
			path = CORPUS_PATH + file
			with open(path, 'rb') as open_file:
				tokens = self._digest_handle(open_file)
				self.documents.append(tokens)
				texts.append(tokens)


		self.dictionary = corpora.Dictionary(self.documents)
		self.dictionary.save(DICT_SAVE_PATH)

		self.corpus = [self.dictionary.doc2bow(text) for text in texts]
		corpora.SvmLightCorpus.serialize(CORPUS_SAVE_PATH, self.corpus)

	

	def _digest_handle(self, file):

		new_tokens = []

		for line in file:
			tokens = line.lower().split()
			for token in tokens:
				if self._clean(token):
					new_tokens.append(token)

		return new_tokens


	def _clean(self, token):
		for letter in token:
			if ord(letter) == 128:
				return False

		return True


