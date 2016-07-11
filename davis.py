play = True
while play is True:

    operation = raw_input("Do you want to add, subtract, multiply, or divide?")
    number1 = int(raw_input("Enter a number"))
    number2 = int(raw_input("Enter another number"))
    if operation == "add":
        print number1 + number2
    elif operation == "subtract":
        print number1 - number2
    elif operation == "multiply":
        print number1 * number2
    elif operation == "divide":
        print float(number1)/float(number2)
    else:
        print "You did not provide a valid operation"
    playAgain = raw_input("Do you want to play again?(y/n)")
    if playAgain == "n":
        play = False
    elif playAgain == "y":
        play = True
    else:
        play = False
