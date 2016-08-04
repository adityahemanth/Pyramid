'''
DESC.  : The core data-structure that makes up the heirarchy of
		 the tree. It takes in an file (JSON) of the tree-structure 
		 and reproduces it with node objects. 

USAGE  : python tree.py


AUTHOR : Hemanth Aditya
'''


from node import node
import json
from utils.search import search

class tree:

	def __init__(self, file):
		with open(file, 'rb') as open_file:
			self.tree_list = json.load(open_file)

		self._initialize()


	def _initialize(self):
		self.root = node('1', 'Root')
		self.root.setChildren( self._branch(self.root, self.tree_list) )


	def _branch(self, parent, nodes):

		if not nodes:
			return

		node_list = []

		for child in nodes:
			new_node = node(child[0], child[1])
			new_node.setChildren( self._branch(new_node, child[2]) )
			new_node.setParent(parent)
			node_list.append(new_node)

		return node_list


	def getNode(self, LCCN):
		return self._traverse(self.root, LCCN)


	def _traverse(self, curr_node, LCCN):

		if not curr_node:
			return

		srh = search()
		if srh.contains(curr_node.getLCCN(), LCCN):
			children = curr_node.getChildren()
			if children:
				for child in children:
					ret_node = self._traverse(child, LCCN)
					if ret_node:
						return ret_node

			return curr_node


	def save(self):
		self._recursive_save(self.root)


	def _recursive_save(self, node):

		if not node:
			return

		if node.children != None:
			for child in node.children:
				self._recursive_save(child)

		node.save()


	
