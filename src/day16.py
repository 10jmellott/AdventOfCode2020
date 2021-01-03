import re

def _load_file():
	# Open the file in read-only mode
	return open('data/16.txt', 'r')


class Field:
	def __init__(self, field):
		result = re.search(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', field)
		self.name = result.group(1)
		ranges = []
		ranges.append([int(result.group(2)), int(result.group(3))])
		ranges.append([int(result.group(4)), int(result.group(5))])
		self.ranges = ranges
		self.indices = []

	def isValid(self, value):
		for r in self.ranges:
			if value >= r[0] and value <= r[1]:
				return True
		return False

class Ticket:
	def __init__(self, values):
		self.values = list(map(lambda v: int(v), values.split(',')))


def _parseInput(f):
	fields = []
	setMyTicket = False
	myTicket = None
	tickets = None
	for line in f.readlines():
		line = line.replace('\n', '')
		if not line or line == '':
			continue
		if line == 'your ticket:':
			setMyTicket = True
		elif setMyTicket:
			myTicket = Ticket(line)
			setMyTicket = False
		elif line == 'nearby tickets:':
			tickets = []
		elif tickets != None:
			tickets.append(Ticket(line))
		else:
			fields.append(Field(line))
	return fields, myTicket, tickets


def _part1():
	f = _load_file()
	fields, _, tickets = _parseInput(f)
	invalidTotal = 0
	for ticket in tickets:
		for value in ticket.values:
			isValid = False
			for field in fields:
				if field.isValid(value):
					isValid = True
			if not isValid:
				invalidTotal = invalidTotal + value
	return invalidTotal


def _getValidTickets(fields, tickets):
	validTickets = []
	for ticket in tickets:
		isValidTicket = True
		for value in ticket.values:
			isValidValue = False
			for field in fields:
				if field.isValid(value):
					isValidValue = True
			if not isValidValue:
				isValidTicket = False
				break
		if isValidTicket:
			validTickets.append(ticket)
	return validTickets

def _findFieldIndices(fields, tickets):
	for i in range(len(tickets[0].values)):
		for field in fields:
			isMatch = True
			for ticket in tickets:
				if not field.isValid(ticket.values[i]):
					isMatch = False
					break
			if isMatch:
				field.indices.append(i)

def _reduceFields(fields):
	reduced = True
	while reduced:
		reduced = False
		for field in fields:
			if len(field.indices) == 1:
				for altField in fields:
					if field == altField:
						continue
					if field.indices[0] in altField.indices:
						altField.indices.remove(field.indices[0])
						reduced = True


def _part2():
	f = _load_file()
	fields, myTicket, tickets = _parseInput(f)
	validTickets = _getValidTickets(fields, tickets)
	_findFieldIndices(fields, validTickets)
	_reduceFields(fields)

	myTicketProduct = 1
	for field in fields:
		if 'departure' in field.name:
			myTicketProduct = myTicketProduct * myTicket.values[field.indices[0]]

	return myTicketProduct


def main():
	return _part1(), _part2()
