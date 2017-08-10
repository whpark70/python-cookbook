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