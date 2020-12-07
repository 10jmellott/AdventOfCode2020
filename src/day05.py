import re


def _load_file():
	# Open the file in read-only mode
	return open('data/05.txt', 'r')


def _parseSeat(seat):
	seat = seat.replace('\n', '')
	rowPart = seat[0:7].replace('B', '1').replace('F', '0')
	colPart = seat[-3:].replace('R', '1').replace('L', '0')
	row = int(rowPart, 2)
	col = int(colPart, 2)
	return seat, row, col, row * 8 + col


def _part1():
	f = _load_file()
	maxSeatId = -1
	minSeatId = 10000
	for line in f.readlines():
		seatId = _parseSeat(line)[3]
		maxSeatId = max(maxSeatId, seatId)
		minSeatId = min(minSeatId, seatId)
	return minSeatId, maxSeatId


def _part2():
	f = _load_file()
	validSeats = []
	for line in f.readlines():
		seat = _parseSeat(line)
		validSeats.append(seat[3])
	seatIdRange = _part1()
	for seatId in range(seatIdRange[0], seatIdRange[1]):
		if not seatId in validSeats:
			if seatId - 1 in validSeats:
				if seatId + 1 in validSeats:
					return seatId
	return -1


def main():
	return _part1(), _part2()
