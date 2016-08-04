'''
USAGE : python main.py

DESC  : dRun this main class with the following arguments:

		i) '-e' : To extract new keywords from MARC records
                  and update the document corpus

        ii) '-i' : To use the document corpus to build document
                   indices and dictionary for 'LSI'

        iii) '-t' : To train a new if-tdif model

'''

import sys, os
from training import *

DATASET_PATH = 'training/datasets'
CORPUS_PATH = 'hierarchy/corpus'

def extract():

	files = os.listdir(DATASET_PATH)
	print 'Found ', len(files), 'files'
	print 'Extracting ... '

	if len(files) == '0':
		print 'datasets not found'
		print 'copy training data to "training/datasets" '

	obj_ext = extractor()
	obj_ext.extract()



def digest():
	obj_dig = digester()
	obj_dig.digest()




def main():

	arg_list = sys.argv

	if '-e' in arg_list:
		extract()
		print 'Extraction complete'

	if '-i' in arg_list:
		digest()
		print 'Indexing complete'



if __name__ == "__main__":
	main()