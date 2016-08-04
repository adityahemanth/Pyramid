import os, sys
from gensim import corpora

PATH = 'hierarchy/corpus'

class corpus_iterator:

	def __iter__(self):

		docs = ['Human machine interface for lab abc computer applications',
				'A survey of user opinion of computer system response time',
				'The EPS user interface management system',
				'System and human system engineering testing of EPS']


		texts = [[word.lower() for word in doc] for doc in docs ]
		print texts
		dictionary = corpora.Dictionary(texts)

		files = os.listdir(PATH)
		for file in files:
			with open(PATH + '/' + file, 'rb') as open_file:
				content = open_file.readlines()
				for line in content:
					try:
						yield dictionary.doc2bow(line.lower().split())

					except:
						print 'Decoding failed'


