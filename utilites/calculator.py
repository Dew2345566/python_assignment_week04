def add(a,b):
	return a + b
def subtract(a,b):
	return a - b 
def multiply(a,b):
	return a * b
def divide(a,b):
	if b == 0:
		return "Cannot divide by zero"
	return a / b
if __name__ == "__main__":
	x = 10
	y = 5
	print(f"Addition: {add(x, y)}")
	print(f"Subtraction: {subtract(x, y)}")
	print(f"Multiplication: {multiply(x, y)}")
	print(f"Division: {divide(x, y)}")