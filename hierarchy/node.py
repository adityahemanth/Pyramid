import collections
import json
import utils

class node(object):

	def __init__(self, LCCN = '', desc = '', parent = None, children = []):
		self.LCCN = LCCN
		self.parent = parent
		self.children = children
		self.desc = desc
		self.document = []


	def addChild(self, child):
		self.children.append(child)

	def setChildren(self, children):
		self.children = children


	def _isLeaf(self):
		if self.children == []:
			return True
		return False


	def addWord(self, word):
		self.document.append(word)


	def save(self):

		if self._isLeaf:
			with open( self.LCCN + '.json', 'wb' ) as save:
				json.dump(self.document, save, indent = 4)


	# getters and setters
	def getDesc(self):
		return self.desc


	def setDesc(self, desc):
		self.desc = desc


	def getParent(self):
		return self.parent


	def getLCCN(self):
		return self.LCCN


	def setLCCN(self, LCCN):
		self.LCCN = LCCN


	def setParent(self, parent):
		self.parent = parent


	def getChildren(self):
		return self.children


	# debugging
	def print_ancestory(self):
		if not self.LCCN == '1':
			self.parent.print_ancestory()

		print self.LCCN, self.desc

