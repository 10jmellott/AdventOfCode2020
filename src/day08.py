def _load_file():
	# Open the file in read-only mode
	return open('data/08.txt', 'r')


def _parseInstruction(f):
	instructions = []
	for line in f.readlines():
		line = line.replace('\n', '')
		split = line.split(' ')
		instructions.append((split[0], int(split[1])))
	return instructions


def _runInstructions(instructions):
	executedInstructions = set()
	accumulator = 0
	currentInstruction = 0
	n = len(instructions)
	while (not currentInstruction in executedInstructions) and (currentInstruction < n):
		instruction = instructions[currentInstruction]
		executedInstructions.add(currentInstruction)
		if instruction[0] == 'nop':
			currentInstruction = currentInstruction + 1
		elif instruction[0] == 'acc':
			accumulator = accumulator + instruction[1]
			currentInstruction = currentInstruction + 1
		elif instruction[0] == 'jmp':
			currentInstruction = currentInstruction + instruction[1]
	if currentInstruction >= n:
		return (accumulator, 0)
	return (accumulator, 1)


def _part1():
	f = _load_file()
	instructions = _parseInstruction(f)
	return _runInstructions(instructions)[0]


def _part2():
	f = _load_file()
	instructions = _parseInstruction(f)
	for i in range(len(instructions)):
		instruction = instructions[i]
		if instruction[0] == 'nop':
			instructions[i] = ('jmp', instruction[1])
		elif instruction[0] == 'jmp':
			instructions[i] = ('nop', instruction[1])
		result = _runInstructions(instructions)
		if result[1] == 0:
			return result[0]
		if instruction[0] == 'nop':
			instructions[i] = ('nop', instruction[1])
		elif instruction[0] == 'jmp':
			instructions[i] = ('jmp', instruction[1])
	return None


def main():
	return _part1(), _part2()
