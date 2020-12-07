def _load_file():
	# Open the file in read-only mode
	return open('data/06.txt', 'r')


def _parseGroups(f):
	groups = []
	for group in f.read().split('\n\n'):
		groups.append(_parseGroup(group))
	return groups


def _parseGroup(group):
	members = []
	for groupMember in group.split('\n'):
		member = set()
		for option in groupMember:
			member.add(option)
		members.append(member)
	return members


def _part1():
	f = _load_file()
	groups = _parseGroups(f)
	count = 0
	for group in groups:
		overall = set()
		for member in group:
			for option in member:
				overall.add(option)
		count = count + len(overall)
	return count


def _part2():
	f = _load_file()
	groups = _parseGroups(f)
	count = 0
	for group in groups:
		groupOptions = set()
		for option in group[0]:
			groupOptions.add(option)
		for member in group[1:]:
			toRemove = []
			for option in groupOptions:
				if not option in member:
					toRemove.append(option)
			for option in toRemove:
				groupOptions.remove(option)
		count = count + len(groupOptions)
	return count


def main():
	return _part1(), _part2()
