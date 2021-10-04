digit_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operation_characters = ['+', '*']

class AstNode:
	raw = ''
	value = None
	children = []
	operations = []

	def __init__(self, input):
		self.raw = input
		self.value = None
		self.children = []
		self.operations = []
		nestedParens = 0
		currentChild = ''
		for c in input:
			if c == '(':
				if nestedParens > 0:
					currentChild += c
				nestedParens += 1
			elif nestedParens > 0 and c == ')':
				nestedParens -= 1
				if nestedParens == 0:
					self.children.append(AstNode(currentChild))
					currentChild = ''
				else:
					currentChild += c
			elif nestedParens > 0:
				currentChild += c
			elif c == ' ':
				if currentChild != '':
					self.children.append(AstNode(currentChild))
					currentChild = ''
			elif c in operation_characters:
				self.operations.append(c)
			else:
				currentChild += c
		if currentChild != '':
			if len(self.children) > 0:
				self.children.append(AstNode(currentChild))
			else:
				self.value = int(currentChild)

	def evaluate(self):
		if self.value != None:
			return self.value
		self.value = self.children[0].evaluate()
		for i in range(1, len(self.children)):
			childVal = self.children[i].evaluate()
			if self.operations[i - 1] == '+':
				self.value += childVal
			elif self.operations[i - 1] == '*':
				self.value *= childVal
		return self.value

	def evaluateAdvanced(self):
		if self.value != None:
			return self.value
		subchildren = list(map(lambda e: e.evaluateAdvanced(), self.children))
		suboperations = list(self.operations)
		while '+' in suboperations:
			index = suboperations.index('+')
			suboperations.pop(index)
			value = subchildren[index] + subchildren[index + 1]
			subchildren.pop(index)
			subchildren.pop(index)
			subchildren.insert(index, value)
		self.value = 1
		for child in subchildren:
			self.value *= child
		return self.value



def _load_file():
	# Open the file in read-only mode
	return open('data/18.txt', 'r')


def parseInput(f):
	equations = []
	for line in f.readlines():
		equations.append(AstNode(line.rstrip('\n')))
	return equations


def _part1():
	f = _load_file()
	equations = parseInput(f)
	total = 0
	for e in equations:
		total += e.evaluate()
	return total


def _part2():
	f = _load_file()
	equations = parseInput(f)
	total = 0
	for e in equations:
		total += e.evaluateAdvanced()
	return total


def main():
	return _part1(), _part2()
