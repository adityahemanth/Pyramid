# test for stat_save function in hierarchy.tree class
# has to print the MARC record contribution statistics for
# all the nodes in the tree

from hierarchy import tree

LCC_PATH = 'resources/lcc.json'

def test():

	t = tree(LCC_PATH)
	t.save_stats()


