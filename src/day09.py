def _load_file():
	# Open the file in read-only mode
	return open('data/09.txt', 'r')


def _mapValues(f):
	return list(map(lambda a: int(a.replace('\n', '')), f.readlines()))


N = 25


def _part1():
	f = _load_file()
	values = _mapValues(f)
	preamble = values[:N]
	for value in values[N:]:
		success = False
		for a in preamble:
			if success:
				break
			for b in preamble:
				if a == b:
					continue
				success = a + b == value
				if success:
					break
		if not success:
			return value
		for i in range(N - 1):
			preamble[i] = preamble[i + 1]
		preamble[N - 1] = value




def _part2():
	f = _load_file()
	values = _mapValues(f)
	target = _part1()

	for start in range(len(values) - 1):
		for end in range(start + 1, len(values)):
			if sum(values[start:end]) == target:
				return min(values[start:end]) + max(values[start:end])


def main():
	return _part1(), _part2()
