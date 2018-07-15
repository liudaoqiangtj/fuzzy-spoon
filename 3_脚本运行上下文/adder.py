#! /usr/bin/env python
import sys
#adder1.py
# sum = 0
# while True:
# 	try:
# 		line = input()
# 	except EOFError:
# 		break
# 	else:
# 		sum += int(line)
# print(sum)

# adder2.py
# sum = 0
# while True:
# 	line = sys.stdin.readline()
# 	if not line: break
# 	sum += int(line)
# print(sum)

#adder3.py
# sum = 0
# for line in sys.stdin.readlines(): sum += int(line)
# print(sum)

#adder4.py
import sys
print(sum(int(line)) for line in sys.stdin)