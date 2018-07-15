def interact():
	print('Hello stream world')
	while True:
		try:
			reply = input('Enter a number>')
		except EOFError:
			break
		else:
			num = int(reply)
			print("%d squared is %d" %(num,num ** 2))
	print('Bye')
if __name__ == '__main__':
	# interact()
	from redirect import redirect
	(result, output) = redirect(interact, (), {},'4\n5\n6\n')
	print(result)
	print(output)
	for line in output.splitlines():print(line)