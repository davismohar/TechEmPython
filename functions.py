def add(n1, n2):
    print n1+n2
def subtract(n1, n2):
    print n1-n2
def mutliply(n1, n2):
    print n1*n2
def divide(n1, n2):
    print float(n1)/float(n2)

operation = raw_input("Would you like to add, subtract, multiply, or divide?")
number1 = raw_input("Enter the first number")
number2 = raw_input("Enter the second number")

if operation == "add":
    add(number1, number2)
elif operation == "subtract":
    subtract(number1, number2)
elif operation == "mutiply":
    mutiply(number1, number2)
elif operation == "divide":
    divide(number1, number2)
