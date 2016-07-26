from hierarchy import *
from utils import *

def runtest():

	print 'contains test'

	sch = search()
	print sch.contains('TL500-777','TL589 .I48 subser')
	t = tree('resources/lcc.json')

	node = t.getNode('TL589 .I48 subser')

	print 'LCCN', node.getLCCN()
	print 'Parent', node.getParent().getLCCN()

	node.print_ancestory()