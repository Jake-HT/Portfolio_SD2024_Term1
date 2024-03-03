loop = 1
while loop == 1:
    startingInput = input('Would you like to Add(1), Subtract(2), Divide(3) or Multiply(4)? Or enter 0 to close the program!: ')
    if startingInput == '1':
        print('You have chosen Addition!')
        num1 = float(input("Enter first number to add: "))
        num2 = float(input("Enter second number to add: "))
        print('The result is: ', num1 + num2, ' !')
    elif startingInput == '2':
        print('You have chosen Subtraction!')
        num1 = float(input("Enter first number to add: "))
        num2 = float(input("Enter second number to add: "))
        print('The result is: ', num1 - num2, ' !')
    elif startingInput == '3':
        print('You have chosen Division!')
        num1 = float(input("Enter first number to add: "))
        num2 = float(input("Enter second number to add: "))
        print('The result is: ', num1 / num2, ' !')
    elif startingInput == '4':
        print('You have chosen Multiplication!')
        num1 = float(input("Enter first number to add: "))
        num2 = float(input("Enter second number to add: "))
        print('The result is: ', num1 * num2, ' !')
    elif startingInput == '0':
        print('Thank you for using Calcoolator!! ')
        loop = 0
    else:
        print('Please enter a valid input! ')