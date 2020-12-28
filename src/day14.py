import re


def _load_file():
	# Open the file in read-only mode
	return open('data/14.txt', 'r')


def setBit(value, bit):
	return value | (1 << bit)

def clearBit(value, bit):
	return value & ~(1 << bit)

def _decoderv1(memory, op, mask):
	value = op[1]
	i = len(mask) - 1
	for bit in mask:
		if bit == '1':
			value = setBit(value, i)
		elif bit == '0':
			value = clearBit(value, i)
		i = i - 1
		memory[op[0]] = value


def _checkBit(valueBit, maskBit):
	if maskBit == 'X' or maskBit == '1':
		return maskBit
	return valueBit

def _applyMask(value, mask):
	value = '{0:b}'.format(value)
	n = len(value)
	maskLen = len(mask)
	for i in range(n):
		maskIndex = maskLen - n + i
		bit = _checkBit(value[i], mask[maskIndex])
		mask = mask[:maskIndex] + bit + mask[maskIndex+1:]
	return mask

def _getFloatingAddresses(addr, addresses):
	for i in range(len(addr)):
		val = addr[i]
		if val == 'X':
			_getFloatingAddresses(addr[:i] + '1' + addr[i + 1:], addresses)
			_getFloatingAddresses(addr[:i] + '0' + addr[i + 1:], addresses)
			return addresses
	addresses.append(int(addr, 2))
	return addresses

def _decoderv2(memory, op, mask):
	address = _applyMask(op[0], mask)
	floatingAddresses = _getFloatingAddresses(address, [])
	for addr in floatingAddresses:
		memory[addr] = op[1]


def _parseInput(f, decoder):
	mask = ''
	memory = dict()
	for line in f.readlines():
		line = line.replace('\n', '')
		if line.startswith('mask'):
			mask = line.replace('mask = ', '')
		else:
			opCapture = re.search(r'mem\[(\d+)\] = (\d+)', line)
			op = (int(opCapture.group(1)), int(opCapture.group(2)))
			decoder(memory, op, mask)
	return sum(memory[v] for v in memory)


def _part1():
	f = _load_file()
	return _parseInput(f, _decoderv1)


def _part2():
	f = _load_file()
	return _parseInput(f, _decoderv2)


def main():
	return _part1(), _part2()
