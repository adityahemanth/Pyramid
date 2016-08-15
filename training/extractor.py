from hierarchy import *
from utils import *
import os, sys
from pymarc import *
import json

DATASET_PATH = 'training/datasets'
TREE_PATH = 'resources/lcc.json'
STATS_PATH = 'stats/'


class extractor:

	def __init__(self):
		self.tree = tree(TREE_PATH)
		self.dataset_path = DATASET_PATH
		self.record_count = 0


	def extract(self):

		files = os.listdir( self.dataset_path )
		x = len(files)
		c = 0
		for file in files:
			print 'reading : ', file
			abs_path = self.dataset_path + '/' + file
			with open(abs_path , 'rb') as marc_record:
				reader = MARCReader(marc_record)
				self._process(reader)
			c += 1
			print 'extraction completed ... ', c * 100 / x , '%'

			marc_list = self.tree.save_stats()
			with open(os.path.join(STATS_PATH, 'stats.json'), 'wb') as stat_file:
				json.dump(marc_list, stat_file, indent=4)

			print self.record_count




	def _process(self, reader):

		search_obj =  search()
		counter = 0

		try:
			for record in reader:
				counter += 1
				if record['050']:
					call = record['050'].format_field()
					if search_obj.validate( call ):
						node = self.tree.getNode(call)
						self._save_record(node, record)

				if counter == 10000:
					self.tree.save()
					counter = 0

		except:
			print 'Error reading: ignoring record'



	def _save_record(self, node, record):

		if not (node or record):
			return

		c_obj = check()

		if not node._isTopLevel():
			if record.title():

				# gathering usage statistics
				self.record_count += 0

				title = record.title().split()
				for word in title:
					if c_obj._validate_word(word):
						word = c_obj._clean_word(word)
						node.addWord(word.lower())

				node.incrementMARCcount()




	

