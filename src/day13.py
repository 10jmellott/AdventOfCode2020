def _load_file():
	# Open the file in read-only mode
	return open('data/13.txt', 'r')


def _part1():
	f = _load_file()
	earliestDeparture = int(f.readline())
	busses = list(map(lambda a: int(a), f.readline().replace(',x', '').split(',')))
	earliestBus = (busses[0], earliestDeparture + busses[0] - (earliestDeparture % busses[0]))
	for bus in busses[1:]:
		nextDeparture = earliestDeparture + bus - (earliestDeparture % bus)
		if nextDeparture < earliestBus[1]:
			earliestBus = (bus, nextDeparture)
	return earliestBus[0] * (earliestBus[1] - earliestDeparture)


# Full disclosure, I spent way too much time trying to
#   solve congruence equations by hand which led to me
#   giving up and copying this solution from someone else
def _part2():
	f = _load_file()
	f.readline() # discard value
	busses = f.readline().split(',')
	minute = 0
	increment = 1
	for i in range(len(busses)):
		if busses[i] != 'x':
			bus = int(busses[i])
			# Find the next value divisible by the bus number
			while (minute + i) % bus != 0:
				minute = minute + increment
			 # Must be divisible by ALL prior bus numbers
			 # This only works as all bus numbers are prime
			increment *= bus
	return minute


def main():
	return _part1(), _part2()
