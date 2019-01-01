
def calc(x, y, ops):
    """
    Returns a string like this: a op b = c
    where c is the computed value according to the opeartor
    """

    if ops not in '+-/*':
        return 'Please only type one of these characters: "+, -, *, /"!'

    if ops == '+':
        return(str(x) + ' ' + ops + ' ' + str(y) + ' = ' + str(x + y))
    if ops == '-':
        return(str(x) + ' ' + ops + ' ' + str(y) + ' = ' + str(x - y))
    if ops == '*':
        return(str(x) + ' ' + ops + ' ' + str(y) + ' = ' + str(x * y))
    if ops == '/':
        return(str(x) + ' ' + ops + ' ' + str(y) + ' = ' + str(x / y))

while True:

	x = int(input('Please type the first number: '))
	y = int(input('Please type the second number: '))
	ops = input("Choose between +, -, *, / ")

	print(calc(x, y, ops))

