from io import FileIO


def _load_file():
	# Open the file in read-only mode
	return open('data/17.txt', 'r')


def parseInput(f):
	active = set()
	column = 0
	row = 0
	for c in f.read():
		if c is '\n':
			column = 0
			row += 1
		else:
			if c is '#':
				active.add((column, row, 0, 0))
			column += 1
	return active

def getNeighbors3D(cell):
	neighbors = set()
	for x in range(cell[0] - 1, cell[0] + 2):
		for y in range(cell[1] - 1, cell[1] + 2):
			for z in range(cell[2] - 1, cell[2] + 2):
				if x is cell[0] and y is cell[1] and z is cell[2]:
					continue
				neighbors.add((x, y, z, 0))
	return neighbors

def _part1():
	f = _load_file()
	active = parseInput(f)
	for i in range(6):
		hotNeighbors = set()
		newActive = set()
		for cell in active:
			neighbors = getNeighbors3D(cell)
			inactiveNeighbors = list(filter(lambda n: n not in active, neighbors))
			if len(inactiveNeighbors) == 23 or len(inactiveNeighbors) == 24:
				newActive.add(cell)
			hotNeighbors.update(inactiveNeighbors)
		for cell in hotNeighbors:
			neighbors = getNeighbors3D(cell)
			activeNeighbors = list(filter(lambda n: n in active, neighbors))
			if len(activeNeighbors) == 3:
				newActive.add(cell)
		active = newActive
	print(len(active))
	return None


def getNeighbors4D(cell):
	neighbors = set()
	for x in range(cell[0] - 1, cell[0] + 2):
		for y in range(cell[1] - 1, cell[1] + 2):
			for z in range(cell[2] - 1, cell[2] + 2):
				for w in range(cell[3] - 1, cell[3] + 2):
					if x is cell[0] and y is cell[1] and z is cell[2] and w is cell[3]:
						continue
					neighbors.add((x, y, z, w))
	return neighbors


def _part2():
	f = _load_file()
	active = parseInput(f)
	for i in range(6):
		hotNeighbors = set()
		newActive = set()
		for cell in active:
			neighbors = getNeighbors4D(cell)
			inactiveNeighbors = list(filter(lambda n: n not in active, neighbors))
			if len(inactiveNeighbors) == 77 or len(inactiveNeighbors) == 78:
				newActive.add(cell)
			hotNeighbors.update(inactiveNeighbors)
		for cell in hotNeighbors:
			neighbors = getNeighbors4D(cell)
			activeNeighbors = list(filter(lambda n: n in active, neighbors))
			if len(activeNeighbors) == 3:
				newActive.add(cell)
		active = newActive
	print(len(active))
	return None


def main():
	return _part1(), _part2()
