"""Run.py
A startup location to execute all problems
"""

from shared import stopwatch
from src import day19

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
test(day19.main, "Day 19")
