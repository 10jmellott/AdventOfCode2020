import re


def _load_file():
	# Open the file in read-only mode
	return open('data/04.txt', 'r')


def _parsePassports(f):
	passports = []
	for passportStr in f.read().split('\n\n'):
		passportStr = passportStr.replace('\n', ' ')
		matches = re.findall(r'([a-z]+):([#\w]+) *', passportStr)
		currentPassport = dict()
		for match in matches:
			currentPassport[match[0]] = match[1]
		passports.append(currentPassport)
	return passports


requiredKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
def _validatePassportKeys(passport):
	for key in requiredKeys:
		containsKey = key in passport
		if not containsKey:
			return False
	return True

def _validateYear(year, minYear, maxYear):
	if re.search(r'\d\d\d\d', year) != None:
		year = int(year)
		return year >= minYear and year <= maxYear
	return False

def _validateHeight(height):
	match = re.search(r'^(\d+)(cm|in)$', height)
	if match != None:
		value = int(match.group(1))
		unit = match.group(2)
		if unit == 'cm':
			return value >= 150 and value <= 193
		if unit == 'in':
			return value >= 59 and value <= 76
	return False


def _validateHairColor(hairColor):
	match = re.search(r'^#[0-9|a-f]{6}$', hairColor)
	return match != None


def _validateEyeColor(eyeColor):
	match = re.search(r'^(amb|blu|brn|gry|grn|hzl|oth)$', eyeColor)
	return match != None


def _validatePassportId(pid):
	match = re.search(r'^\d{9}$', pid)
	return match != None


def _validatePassportValues(passport):
	valid = True
	valid = valid and _validateYear(passport['byr'], 1920, 2002)
	valid = valid and _validateYear(passport['iyr'], 2010, 2020)
	valid = valid and _validateYear(passport['eyr'], 2020, 2030)
	valid = valid and _validateHeight(passport['hgt'])
	valid = valid and _validateHairColor(passport['hcl'])
	valid = valid and _validateEyeColor(passport['ecl'])
	valid = valid and _validatePassportId(passport['pid'])
	return valid


def _part1():
	f = _load_file()
	passports = _parsePassports(f)
	validPassports = 0
	for passport in passports:
		if _validatePassportKeys(passport):
			validPassports = validPassports + 1
	return validPassports


def _part2():
	f = _load_file()
	passports = _parsePassports(f)
	validPassports = 0
	for passport in passports:
		if _validatePassportKeys(passport) and _validatePassportValues(passport):
			validPassports = validPassports + 1
	return validPassports


def main():
	return _part1(), _part2()
