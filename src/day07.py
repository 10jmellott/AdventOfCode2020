import re


def _load_file():
	# Open the file in read-only mode
	return open('data/07.txt', 'r')


def _parseRules(f):
	rules = dict()
	for line in f.readlines():
		line = line.replace('\n', '')
		split = line.split(' contain ')
		target = re.search('(.+) bags', split[0]).group(1)
		targetRules = dict()
		targetRuleParts = split[1].split(',')
		for targetRule in targetRuleParts:
			if targetRule == 'no other bags.':
				continue
			targetRuleResult = re.search(r'(\d+) (.+) bag', targetRule)
			targetRules[targetRuleResult.group(2)] = int(targetRuleResult.group(1))
		rules[target] = targetRules
	return rules


def _part1():
	f = _load_file()
	rules = _parseRules(f)
	containingColors = set()
	toCheck = ['shiny gold']
	while len(toCheck) > 0:
		check = toCheck.pop()
		for key in rules:
			for rule in rules[key]:
				if rule == check:
					containingColors.add(key)
					toCheck.append(key)
	return len(containingColors)


def _part2():
	f = _load_file()
	rules = _parseRules(f)
	bags = 0
	toCheck = ['shiny gold']
	while len(toCheck) > 0:
		check = toCheck.pop()
		for rule in rules[check]:
			count = rules[check][rule]
			bags = bags + count
			for _ in range(count):
				toCheck.append(rule)
	return bags

def main():
	return _part1(), _part2()
