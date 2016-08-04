# Pyramid

An information retrieval engine that leverages LSA (Latent Semantic Analysis) and LLC (Library of Congress Classification) to categorize and retrieve documents


## USAGE:

1) SETUP:

	1.1 Copy training datasets - MARC records ( ending in .mrc ) into datasets folder under training. 
	FOLDER : 'Pyramid/training/datasets'


	1.2 run main.py file with -e, -i flags to extract keywords from the training dataset and build indeices for LSI.
	
	```python
	python main.py -e -i
	```


2) RUNNING:

	
	2.1 import 'similarity' from training module and instantiate a search object.

	2.2 Use the search method of the search method of the search object to enter search terms. This returns a node object.


	2.3 Use the node objects methods (getLCCN(), getParent(), getDesc() .. etc ) to retrieve necessary information.
	
	
	```python
	from training import similarity
	# make a search object
	obj_search = search()
	node = obj_search('Computer programming')
	print 'LCC number: ', node.getLCCN()
	print 'Description : ', node.getDesc()
	```

