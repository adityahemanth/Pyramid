'''
Processes the extracted data from the MARC
records into a dictionary of words and frequency
'''
import json
import os, sys
from collections import defaultdict
import operator

CORPUS_PATH = 'hierarchy/corpus'
JSON_PATH = 'resources/frequency'

class processor:

	def __init__(self):
		self.path = CORPUS_PATH
		self.save_path = JSON_PATH


	def process(self):
		
		files = os.listdir(self.path)
		for file in files:
			file_path = os.path.join(self.path, file)
			with open(file_path, 'rb') as open_file:
				self._process_handler(open_file, file)


	def _process_handler(self, file, filename):

		word_freq = defaultdict(int)
		if not file:
			return 

		data = file.read()
		data = data.split('\n')

		for word in data:
			if word != '':
				word_freq[word] += 1

		word_freq = sorted(word_freq.items(), key=lambda x: -x[1])

		try:
			with open( os.path.join(JSON_PATH, filename), 'wb') as save_file:
				json.dump(word_freq, save_file)

		except:
			print 'Failed to write ', file
