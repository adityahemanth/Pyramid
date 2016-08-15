import json
import os, sys
from hierarchy import tree

TREE_PATH = 'resources/lcc.json'
FREQ_PATH = 'resources/frequency'
WORD_LIST = 'stats/'

class ui:

	def __init__(self):

		self.prev_list = []
		self.tree = tree()
		with open(os.path.join(WORD_LIST, 'stats.json'), 'rb') as stats:
			self.stats = json.load(stats)
		self.display(self.tree.root)



	def display(self, node):

		if not node:
			return 

		if not node.children:
			self.open_words(node)

		else:

			print 'Index - LCC Number : Description : MARC records contributed'
			for i in range(len(node.children)):
				child = node.children[i]
				print i, ' - ', child.getLCCN(), ' : ', child.getDesc(), ' : ', self.marc_contribution(child)

		self.get_input(node)



	def get_input(self, curr_node):
		
		if not curr_node:
			return

		entry = self.get_entry()

		if entry == -1:
			if len(self.prev_list) > 0:
				self.display(self.prev_list.pop())
			else:
				self.display(self.tree.root)


		if curr_node.children:
			for i in range(len(curr_node.children)):
				if entry == i:
					self.prev_list.append(curr_node)
					self.display(curr_node.children[i])

		else:
			self.display(curr_node)



	def get_entry(self):
		entry = raw_input('\nEnter node index to browse \n " < " to go back \n')

		if entry == '<':
			return -1

		try:
			entry = int(entry)
			return entry
		except:
			print 'Entry has to be a numeric or " < " '
			return self.get_entry()


	def open_words(self, node):
		
		file = node.getLCCN()
		path = os.path.join(FREQ_PATH, file + '.json')
		with open(path, 'rb') as freq_file:
			words = json.load(freq_file)

		for word in words:
			print word

	def marc_contribution(self, node):
		lccn = node.getLCCN()
		for stat in self.stats:
			if stat[0] == lccn:
				return stat[1]

		return







