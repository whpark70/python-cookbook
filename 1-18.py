from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')

def compute_cost(records):
	total = 0.0
	for rec in records:
		total += rec[1] * rec[2]
	return total

def compute_cost2(records):
	total = 0.0
	for rec in records:
		s = Stock(*rec)
		total += s.shares * s.price
	return total

Stock = namedtuple('Stock', ['name', 'shares', 'price'])


if __name__ == '__main__':
	print(sub, sub.addr, sub.joined)
	print('len: ', len(sub))
	addr, joined = sub
	print('addr: ', addr, ',joined: ',joined)

	s = Stock('ACME', 100, 123.45)
	print(s)
	s = s._replace(shares=75)
	print(s)