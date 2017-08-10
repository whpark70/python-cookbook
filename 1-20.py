a = { 'x': 1, 'z': 3}
b = { 'y': 2, 'z': 4}

from collections import ChainMap
c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])

print('len:', len(c), ',keys: ', list(c.keys()), ',values: ', list(c.values()))

values = ChainMap()
values['x'] = 1
# add a new mapping
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3

print('2nd values: ', values)

print(values['x'])

#discard last mapping
values = values.parents
print(values['x'])

#discard last mapping
values = values.parents
print(values['x'])

print(values)

