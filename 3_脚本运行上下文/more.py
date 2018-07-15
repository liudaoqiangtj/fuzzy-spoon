def more(text,numlines=15):
	lines = text.splitlines()#splitlines()将字符串在换行处分割
	while lines:
		chunk = lines[:numlines]
		lines = lines[numlines:]
		for line in chunk:
			print(line)
		if lines and input('More?') not in ['Y','y']:break
if __name__ == '__main__':
	import sys
	if len(sys.argv) == 1:
		more(sys.stdin.read())
	else:
		more(open(sys.argv[1]).read())

