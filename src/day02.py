import re

def _load_file():
	# Open the file in read-only mode
	return open('data/02.txt', 'r')

def countOccurrence(s, char):
	count = 0
	for c in s:
		if c == char:
			count = count + 1
	return count

def _part1():
	f = _load_file()
	matches = re.findall(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', f.read())
	valid = 0
	for match in matches:
		minRep = int(match[0])
		maxRep = int(match[1])
		char = match[2]
		pw = match[3]
		occurrences = countOccurrence(pw, char)
		if occurrences >= minRep and occurrences <= maxRep:
			valid = valid + 1
	return valid

def _part2():
	f = _load_file()
	matches = re.findall(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', f.read())
	valid = 0
	for match in matches:
		index1 = int(match[0]) - 1
		index2 = int(match[1]) - 1
		char = match[2]
		pw = match[3]
		if pw[index1] == char and pw[index2] != char:
			valid = valid + 1
		elif pw[index1] != char and pw[index2] == char:
			valid = valid + 1
	return valid

def main():
	return _part1(), _part2()
