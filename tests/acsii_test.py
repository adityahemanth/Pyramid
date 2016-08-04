'''
Testing to see whether program eliminated non-acsii chars from corpus
'''

import os, sys, json


# test path
PATH = 'hierarchy/corpus'

def check_acsii(word):

	if not word:
		return

	for letter in word:
		print ord(letter)


def read_file(file):

	with open(abs_path, 'rb') as open_file:

		for word in open_file:
			check_acsii(word)


def check():

	files = os.listdir(PATH)

	for file in files:
		with open(PATH + '/' + file, 'rb') as open_file:
			for f1 in open_file:
				for word in f1:
					print word




	