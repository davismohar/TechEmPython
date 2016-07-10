operation = raw_input("Would you like to add, subtract, mutiply, or divide?")
number1 = int(raw_input("Enter the first number"))
number2 = int(raw_input("Enter the second number"))
if operation == "add":
    answer = number1 + number2
elif operation == "subtract":
    answer = number1 - number2
elif operation == "multiply":
    answer = number1 * number2
elif operation == "divide":
    answer = float(number1)/float(number2)
print answer
