def add (x, y):
    return x + y

def subtract(x, y): 
    return x - y

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero!')
    return a / b

