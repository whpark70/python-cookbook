# filtering sequence elmenents

values = [ '1', '2', '-3', '-', '4', 'N/A','5']

def is_int(val):
	try:
		x = int(val)
		return True
	except ValueError:
		return False

ivals = list(filter(is_int, values))

address = [
	'5412 N CLARK',
	'5418 N CLARK',
	'5800 E 58H',
	'2122 N CLARK',
	'5645 n RAVENSWOOD',
	'1060 W ADDISON',
	'4801 N BORADWAY',
	'1039 W GRANVILLE',
	]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

if __name__ == '__main__':
	
	#print(ivals)
	more5 = [ n > 5 for n in counts]
	print(more5)
	print(list(compress(address, more5)))



