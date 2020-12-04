def _load_file():
	# Open the file in read-only mode
	return open('data/01.txt', 'r')

def _part1():
	f = _load_file()
	data = list(map(lambda l: int(l), f))
	for a in data:
		for b in data:
			if a + b == 2020:
				return a * b

def _part2():
	f = _load_file()
	data = list(map(lambda l: int(l), f))
	for a in data:
		for b in data:
			for c in data:
				if a + b + c == 2020:
					return a * b * c

def main():
	return _part1(), _part2()
