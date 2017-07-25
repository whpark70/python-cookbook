from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)

# Funciton to convert a dictionary to a stock
def dict_to_stock(s):
	return stock_prototype._replace(**s)

a = { 'name': 'ACME', 'shares': 100, 'price': 123.45}
a1 = dict_to_stock(a)
print(a1)