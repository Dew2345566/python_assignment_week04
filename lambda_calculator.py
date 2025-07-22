def add(a,b):
	lambda_func = lambda x, y: x + y
	return lambda_func(a, b)
def subtract(a,b):
	lambda_func = lambda x, y: x - y 
	return lambda_func(a, b)
def multiply(a,b):
	lambda_func = lambda x, y: x * y
	return lambda_func(a, b)
def divide(a,b):
	if b == 0:
		return "Cannot divide by zero"
	lambda_func = lambda x, y: x / y
	return lambda_func(a, b)
if __name__ == "__main__":
	x = 10
	y = 5
	print(f"Addition: {add(x, y)}")
	print(f"Subtraction: {subtract(x, y)}")
	print(f"Multiplication: {multiply(x, y)}")
	print(f"Division: {divide(x, y)}")