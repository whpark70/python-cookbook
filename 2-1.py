line = 'asdf fjdk; afed, fjek,asdf,       foo'

import re
fields = re.split(r'[;,\s]\s*', line)
l2 = re.split(r'(;|,|\s)\s*', line)
#print(fields)
print('fields: ',l2)

values = l2[::2]
print(values)
delimiters = l2[1::2] + ['']
print(delimiters)

joind = ''.join(v+d for v, d in zip(values, delimiters))
print(joind)

fields = re.split(r'(?:,|;|\s)\s*', line)
print(fields)