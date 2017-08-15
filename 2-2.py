filename = 'spam.txt'
extension = filename.endswith('.txt')
print(extension)

ext = filename.startswith('file:')
print(ext)

import os
filenames = os.listdir("..//imsi")
print(filenames)
filtered = [ name for name in filenames if name.endswith(('.c', '.h'))]
print('filtered: ', filtered)

print(any(name.endswith('.py') for name in filenames))


from urllib.request import urlopen

def read_data(name):
	if name.startswith(('http:','https:', 'ftp:')):
		return urlopen(name).read()
	else:
		with open(name) as f:
			return f.read()

