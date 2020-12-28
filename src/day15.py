def _load_file():
	# Open the file in read-only mode
	return open('data/15.txt', 'r')


def _getNextValue(turn, current, indexDict):
	if not current in indexDict:
		return 0
	return turn - indexDict[current]

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
		nextValue = _getNextValue(turn, currentValue, indexDict)
		indexDict[currentValue] = turn
		currentValue = nextValue
	return currentValue


def _part1():
	return play(2020)


def _part2():
	return play(30000000)


def main():
	return _part1(), _part2()
