from hierarchy import *
import os, sys
from pymarc import *

PATH = 'training/datasets'

class trainer:

	def __init__(self):
		self.tree = tree('resources/lcc.json')
		self.path = PATH


	def train(self):
		files = os.listdir( self.path )
		for file in files:
			abs_path = self.path + '/' + file
			with open(abs_path , 'rb') as marc_record:
				reader = MARCReader(marc_record)
				self._process(reader)


	def _process(self, reader):

		for record in reader:
			if record['050']:
				node = self.tree.getNode(record['050'].format_field())
				print node.getLCCN(), ' : ', record['050'].format_field()


	

