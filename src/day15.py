def _load_file():
	# Open the file in read-only mode
	return open('data/15.txt', 'r')


def play(turns):
	f = _load_file()
	initialValues = list(map(lambda v: int(v), f.readline().split(',')))
	indexDict = dict()
	for i in range(len(initialValues) - 1):
		indexDict[initialValues[i]] = i + 1
	turn = len(initialValues) - 1
	currentValue = initialValues[len(initialValues) - 1]
	while turn != turns - 1:
		turn = turn + 1
		age = indexDict.get(currentValue, turn)
		indexDict[currentValue] = turn
		currentValue = turn - age
	return currentValue


def _part1():
	return play(2020)


def _part2():
	return play(30000000)


def main():
	return _part1(), _part2()
