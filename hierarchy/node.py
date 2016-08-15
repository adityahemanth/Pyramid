'''
DESC.  : An object that contains data of individual nodes that make-up
	     the hierarchy

FUNC   : Stores node data. 

USAGE  : Not to be used independently

AUTHOR : Hemanth Aditya
'''


import collections
import json
import os, sys
import utils

SAVE_PATH = 'corpus/'


class node(object):

	def __init__(self, LCCN = '', desc = '', parent = None, children = []):
		self.LCCN = LCCN
		self.parent = parent
		self.children = children
		self.desc = desc
		self.marc_count = 0
		self.document = ''


	def addChild(self, child):
		self.children.append(child)

	def setChildren(self, children):
		self.children = children


	def _isLeaf(self):
		if self.children == []:
			return True
		return False


	def _isRoot(self):
		if self.LCCN == '1':
			return True
		return False

	def _isTopLevel(self):
		if len(self.LCCN) == 1:
			return True
		return False


	def incrementMARCcount(self):
		self.marc_count += 1


	def getMARCcount(self):
		return (self.LCCN, self.marc_count)


	def addWord(self, word):
		self.document += word + '\n'


	def save(self):

		save_string = self.document

		if save_string:
			if not self._isTopLevel():
				with open( os.path.join( 'hierarchy/corpus/', self.LCCN + '.json'), 'wb' )  as save:
					save.write(save_string)


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

