"""Run.py
A startup location to execute all problems
"""

from shared import stopwatch
from src import day05

def test(f, message):
	timer = stopwatch.Timer()
	timer.start()
	ret = f()
	timer.stop()
	print(message)
	if ret:
		print(f'  Solution: {ret}')
	print(f'  Elapsed: {timer.elapsed()}')
	print()

print('Advent of Code - https://adventofcode.com/2020')
print('----------------------------------------------')
print()
test(day05.main, "Day 05")
