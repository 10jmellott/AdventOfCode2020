def _load_file():
	# Open the file in read-only mode
	return open('data/19.txt', 'r')

def parseRule(rawRule):
	parts = rawRule.split(':')
	number = int(parts[0])
	matchingMessages = []
	if parts[1][1] == '"':
		matchingMessages.append(parts[1][2])
	else:
		subrules = parts[1].split('|')
		for subrule in subrules:
			subruleParts = subrule.strip(' ').split(' ')
			matchingMessages.append(list(map(lambda p: int(p), subruleParts)))

	return number, matchingMessages


def parseInput(f):
	rules = []
	messages = None
	for line in f.readlines():
		line = line.rstrip('\n')
		if line == '':
			messages = []
		elif messages != None:
			messages.append(line)
		else:
			rules.append(line)

	parsedRules = {}
	for rule in rules:
		pRule = parseRule(rule)
		parsedRules[pRule[0]] = pRule[1]

	return parsedRules, messages


def resolveRules(ruleNumber, rules, resolvedRules):
	if ruleNumber in resolvedRules:
		return resolvedRules[ruleNumber]
	rulseSets = rules[ruleNumber]
	messages = []
	for rule in rulseSets:
		messageCollection = []
		for item in rule:
			messageCollection.append(resolveRules(item, rules, resolvedRules))
		messages.extend(permutations(messageCollection))

	resolvedRules[ruleNumber] = messages
	return messages


def permutations(list):
	if len(list) == 1:
		return list[0]
	items = []
	subpermutations = permutations(list[1:])
	for item in list[0]:
		for permItem in subpermutations:
			items.append(item + permItem)
	return items

def _part1():
	f = _load_file()
	rules, messages = parseInput(f)

	resolvedRules = {}

	for rule in rules:
		if rules[rule][0] == 'a' or rules[rule][0] == 'b':
			resolvedRules[rule] = rules[rule]

	rule0messages = resolveRules(0, rules, resolvedRules)

	potentialMessages = set(rule0messages)

	successfulMessages = 0
	for message in messages:
		if message in potentialMessages:
			successfulMessages += 1

	return successfulMessages


def _part2():
	f = _load_file()
	rules, messages = parseInput(f)

	rules[8] = [[42], [42, 8]]
	rules[11] = [[42, 31], [42, 11, 31]]

	resolvedRules = {}

	for rule in rules:
		if rules[rule][0] == 'a' or rules[rule][0] == 'b':
			resolvedRules[rule] = rules[rule]

	rule0messages = resolveRules(0, rules, resolvedRules)

	potentialMessages = set(rule0messages)

	successfulMessages = 0
	for message in messages:
		if message in potentialMessages:
			successfulMessages += 1

	return successfulMessages


def main():
	return _part1(), _part2()
