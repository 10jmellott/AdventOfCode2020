def _load_file():
	# Open the file in read-only mode
	return open('data/11.txt', 'r')


def _mapSeats(f):
	rows = []
	for line in f.readlines():
		line = line.replace('\n', '')
		col = []
		for seat in line:
			if seat is '.':
				col.append(None)
			else:
				col.append(False)
		rows.append(col)
	return rows


def _getSeat(seats, i, j):
	if i < 0 or j < 0:
		return None
	if j >= len(seats):
		return None
	if i >= len(seats[j]):
		return None
	return seats[j][i]


def _getAdjacentSeats(seats, i, j):
	adjacent = []
	adjacent.append(_getSeat(seats, i - 1, j - 1))
	adjacent.append(_getSeat(seats, i, j - 1))
	adjacent.append(_getSeat(seats, i + 1, j - 1))
	adjacent.append(_getSeat(seats, i - 1, j))
	adjacent.append(_getSeat(seats, i + 1, j))
	adjacent.append(_getSeat(seats, i - 1, j + 1))
	adjacent.append(_getSeat(seats, i, j + 1))
	adjacent.append(_getSeat(seats, i + 1, j + 1))
	return adjacent


def _findNextSeat(seats, i, j, di, dj):
	i = i + di
	j = j + dj
	while j >= 0 and i >= 0 and j < len(seats) and i < len(seats[j]):
		seat = _getSeat(seats, i, j)
		if _getSeat(seats, i, j) != None:
			return seat
		i = i + di
		j = j + dj
	return None


def _getAdjacentSeats2(seats, i, j):
	adjacent = []
	adjacent.append(_findNextSeat(seats, i, j, -1, -1))
	adjacent.append(_findNextSeat(seats, i, j, 0, -1))
	adjacent.append(_findNextSeat(seats, i, j, 1, -1))
	adjacent.append(_findNextSeat(seats, i, j, -1, 0))
	adjacent.append(_findNextSeat(seats, i, j, 1, 0))
	adjacent.append(_findNextSeat(seats, i, j, -1, 1))
	adjacent.append(_findNextSeat(seats, i, j, 0, 1))
	adjacent.append(_findNextSeat(seats, i, j, 1, 1))
	return adjacent


def _updateSeat(seats, i, j, maxOccupied, getAdjacent):
	# No need to update floor seating
	if seats[j][i] is None:
		return None
	adjacent = getAdjacent(seats, i, j)
	nearbyOccupied =  adjacent.count(True)
	if nearbyOccupied == 0:
		return True
	elif nearbyOccupied >= maxOccupied:
		return False
	return seats[j][i]


def _updateSeats(seats, maxOccupied, getAdjacent):
	rows = []
	for j in range(len(seats)):
		col = []
		for i in range(len(seats[j])):
			col.append(_updateSeat(seats, i, j, maxOccupied, getAdjacent))
		rows.append(col)
	return rows


def _areEqual(seats, newSeats):
	for j in range(len(seats)):
		for i in range(len(seats[j])):
			if seats[j][i] != newSeats[j][i]:
				return False
	return True


def _findEquilibrium(maxOccupied, getAdjacent):
	f = _load_file()
	seats = _mapSeats(f)
	newSeats = _updateSeats(seats, maxOccupied, getAdjacent)
	while not _areEqual(seats, newSeats):
		seats = newSeats
		newSeats = _updateSeats(seats, maxOccupied, getAdjacent)

	occupied = 0
	for row in seats:
		occupied = occupied + row.count(True)
	return occupied


def _part1():
	return _findEquilibrium(4, _getAdjacentSeats)


def _part2():
	return _findEquilibrium(5, _getAdjacentSeats2)


def main():
	return _part1(), _part2()
