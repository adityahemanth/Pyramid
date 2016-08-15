# fucntions to filter information gathered
# during MARC record parsing
import json

STAT_FILE = 'stats.json'

def count():

	with open(STAT_FILE, 'rb') as open_file:
		stats = json.load(open_file)


	sum = 0
	for node in stats:
		sum += node[1]

	print sum, ' records used'


count()
