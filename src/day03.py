from functools import reduce

def _load_file():
	# Open the file in read-only mode
	return open('data/03.txt', 'r')

def parseTreemap(f):
	treemap = []
	for line in f.readlines():
		row = []
		for char in line:
			if char != '\n':
				row.append(char == '#')
		treemap.append(row)
	return treemap

def _countTrees(treemap, dx, dy):
	maxY = len(treemap)
	n = len(treemap[0])
	x = 0
	y = 0
	trees = 0
	while y < (maxY - dy):
		x = x + dx
		x = x % n
		y = y + dy
		if treemap[y][x]:
			trees = trees + 1
	return trees

def _part1():
	f = _load_file()
	treemap = parseTreemap(f)
	return _countTrees(treemap, 3, 1)

def _part2():
	f = _load_file()
	treemap = parseTreemap(f)
	treeCounts = [
		_countTrees(treemap, 1, 1),
		_countTrees(treemap, 3, 1),
		_countTrees(treemap, 5, 1),
		_countTrees(treemap, 7, 1),
		_countTrees(treemap, 1, 2)
	]
	return reduce(lambda a, b: a * b, treeCounts)

def main():
	return _part1(), _part2()
