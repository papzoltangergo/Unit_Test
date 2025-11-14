def sum(a, b):
        return a + b

def substract(a, b):
        return a - b
def multiply(a, b):
        return a * b
def divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero"