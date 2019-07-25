res = 0

retry = 'y'
while retry == 'y':
	print("Input first number: ")
	n1 = int(input())

	print('input math operator')
	op = input()

	print("Input second number: ")
	n2 = int(input())

	if op == "+":
		res = n1+n2
	elif op == "-":
		res = n1-n2
	elif op == "*":
		res = n1*n2
	elif op == "/":
		res = n1/n2
	elif op == "^":
		res = n1**n2
	
	print('{} {} {} = {}'.format(n1, op, n2, res))
	
	print('\n\tRetry? (y/n)\t\r')
	retry = input()
