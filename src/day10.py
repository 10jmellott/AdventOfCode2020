def _load_file():
	# Open the file in read-only mode
	return open('data/10.txt', 'r')


def _mapAdapters(f):
	return list(map(lambda a: int(a.replace('\n', '')), f.readlines()))


def _part1():
	f = _load_file()
	adapters = _mapAdapters(f)
	# Starting Voltage
	adapters.append(0)
	adapters.sort()
	diffs = { 1 : 0, 2 : 0, 3 : 1 }
	current = adapters[0]
	for adapter in adapters[1:]:
		diff = adapter - current
		diffs[diff] = diffs[diff] + 1
		current = adapter
	return diffs[1] * diffs[3]


def _getPermutations(adapters, i, permutations):
	adapter = adapters[i]
	if adapter in permutations:
		return permutations[adapter]
	j = i + 1
	totalPermutations = 0
	nextAdapter = adapters[j]
	while (nextAdapter + 3) >= adapter:
		totalPermutations = totalPermutations + _getPermutations(adapters, j, permutations)
		j = j + 1
		if j >= len(adapters):
			break
		nextAdapter = adapters[j]
	permutations[adapter] = totalPermutations
	return totalPermutations

def _part2():
	f = _load_file()
	adapters = _mapAdapters(f)
	adapters.append(0)
	adapters.append(max(adapters) + 3)
	adapters.sort()
	adapters.reverse()
	permutations = { 0 : 1 }
	return _getPermutations(adapters, 0, permutations)



def main():
	return _part1(), _part2()
