def _load_file():
	# Open the file in read-only mode
	return open('data/12.txt', 'r')


class Ship:
	position = (0, 0)

	def __init__(self, waypoint):
		self.waypoint = waypoint

	def manhattan(self):
		return abs(self.position[0]) + abs(self.position[1])

	def move(self, instruction, moveWaypoint):
		value = int(instruction[1:])
		if instruction[0] == 'F':
			x = self.position[0] + self.waypoint[0] * value
			y = self.position[1] + self.waypoint[1] * value
			self.position = (x, y)
		elif instruction[0] == 'R':
			self.rotateClockwise(value)
		elif instruction[0] == 'L':
			self.rotateCounterClockwise(value)
		if moveWaypoint:
			if instruction[0] == 'N':
				self.waypoint = (self.waypoint[0], self.waypoint[1] - value)
			elif instruction[0] == 'S':
				self.waypoint = (self.waypoint[0], self.waypoint[1] + value)
			elif instruction[0] == 'W':
				self.waypoint = (self.waypoint[0] - value, self.waypoint[1])
			elif instruction[0] == 'E':
				self.waypoint = (self.waypoint[0] + value, self.waypoint[1])
		else:
			if instruction[0] == 'N':
				self.position = (self.position[0], self.position[1] - value)
			elif instruction[0] == 'S':
				self.position = (self.position[0], self.position[1] + value)
			elif instruction[0] == 'W':
				self.position = (self.position[0] - value, self.position[1])
			elif instruction[0] == 'E':
				self.position = (self.position[0] + value, self.position[1])

	def rotateClockwise(self, degrees):
		if degrees != 0:
			self.waypoint = (-self.waypoint[1], self.waypoint[0])
			self.rotateClockwise(degrees - 90)

	def rotateCounterClockwise(self, degrees):
		if degrees != 0:
			self.waypoint = (self.waypoint[1], -self.waypoint[0])
			self.rotateCounterClockwise(degrees - 90)


def _part1():
	f = _load_file()
	ship = Ship((1, 0))
	for line in f.readlines():
		line = line.replace('\n', '')
		ship.move(line, False)
	return ship.manhattan()


def _part2():
	f = _load_file()
	ship = Ship((10, -1))
	for line in f.readlines():
		line = line.replace('\n', '')
		ship.move(line, True)
	return ship.manhattan()


def main():
	return _part1(), _part2()
