loop = 1
while loop == 1:
    userInput = int(input('Would you like to Add(1), Subtract(2), Divide(3) or Multiply(4)? Or enter 0 to close the pwogwam!: '))
    if userInput == 1:
        print('You have chosen Addition!')
        num1 = int(input('Please enter the first number!: '))
        num2 = int(input('Please enter the second number!: '))
        print('The result is: ', num1 + num2, '! ')
    elif userInput == 2:
        print('You have chosen Subtraction!')
        num1 = int(input('Please enter the first number!: '))
        num2 = int(input('Please enter the second number!: '))
        print('The result is: ', num1 - num2, '! ')
    elif userInput == 3:
        print('You have chosen Division!')
        num1 = int(input('Please enter the first number!: '))
        num2 = int(input('Please enter the second number!: '))
        while num2 == 0:
            print('Cannot divide by zero! Please enter another number!')
            num2 = int(input('Please enter the second number!: '))
        print('The result is: ', num1 / num2, '! ')
    elif userInput == 4:
        print('You have chosen Multiplication!')
        num1 = int(input('Please enter the first number!: '))
        num2 = int(input('Please enter the second number!: '))
        print('The result is: ', num1 * num2, '! ')
    elif userInput == 0:
        print('Thank you for using Calculator! ')
        loop = 0
    else:
        print('Please enter a valid input! ')