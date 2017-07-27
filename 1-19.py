nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)

# Determine if any .py files exist in a directory
import os
files = os.listdir('c:\\')
if any(name.endswith('.py') for name in files):
	print('There be python!')
else:
	print('Sorry, no python')


s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

protfolio = [
	{'name': 'GOOG', 'shares': 58},
	{'name': 'YHOO', 'shares': 75},
	{'name': 'AOL', 'shares': 20},
	{'name': 'SCOX', 'shares': 65},
	]

min_shares = min( s['shares'] for s in protfolio)
print(min_shares)
