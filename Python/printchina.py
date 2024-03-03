# Exercise one Input Prompt: Write a program that takes the user's name as input and prints a personalized greeting.
"""
userInput = str(input('What is your first name? '))
print('Hello ', userInput, ', kill yourself NOW!!!!!')
"""
# Exercise two Numeric Input: Create a program that asks the user to enter two numbers and calculates their sum.
"""
num1 = float(input('Please enter a first number!: '))
num2 = float(input('Please enter a second number!: '))
print('The sum of those two numbers is ', num1 + num2, '! ')
"""
# Exercise three Favorite Color: Prompt the user to enter their favorite color and display a message acknowledging their choice.
"""
favouriteColour = str(input('What is your favourite colour?\n'))
print('Seriously,', favouriteColour, '??! Wow! You have terrible taste!!')
"""
# Exercise four Print Multiple Lines: Write a program that prints a message on one line, and then on the next line, prints a different message.
"""
print('One line! \nTwo line!')
"""
# Exercise five Formatted Output: Create a program that prints a sentence with placeholders for the user's name and age.
"""

"""
# Exercise six Repeated Output: Print the message "Hello" five times using a loop.
"""
loop = 5
while loop > 0:
    print('Hello!')
    loop = loop - 1
"""
# Exercise seven Variable Swap: Swap the values of two variables and print the result.
"""
var1 = input('Please enter a first variable! ')
var2 = input('Please enter a second variable! ')
def swap(var1, var2):
    swap1 = var1
    swap2 = var2
    var1 = swap2
    var2 = swap1
    print(var1, var2)
swap(var1,var2)
"""
# Exercise eight Variable Concatenation: Concatenate two strings stored in variables and print the combined string.
"""
string1 = str(input('Please enter a first phrase to concatenate! '))
string2 = str(input('Please enter a second phrase to concatenate! '))
concatenate = string1 + string2
print(concatenate)
"""
# Exercise nine Variable Initialization: Declare a variable to store your age and initialize it with your actual age.
"""
age = int()
age = int(input('How old are you?: '))
print('Wow, only', age ,'years old? You look terrible for your age!')
"""
# Exercise ten Arithmetic Operations: Write a program that takes two numbers as input and performs addition, subtraction, multiplication, and division.
"""
num1 = float(input('Please enter a first number!: '))
num2 = float(input('Please enter a second number!: '))
print('Addition: ', num1 + num2)
print('Subtraction: ', num1 - num2)
print('Division: ', num1 / num2)
print('Multiplication: ', num1 * num2)
"""
# Exercise eleven Comparison Operators: Create a program that compares two numbers and prints whether they are equal or not.
"""
loop = 1
while loop == 1:
    num1 = float(input('Please enter a first number!: '))
    num2 = float(input('Please enter a second number!: '))
    
    if num1 == num2:
        print('Both numbers are equal! ')
    elif num1 != num2:
        print('The numbers are not equal :(')
    else:
        print('eat shit')
        loop = 0
"""
# Exercise twelve String Concatenation: Concatenate two strings and print the result.
"""
string1 = str(input('Please enter a first phrase to concatenate! '))
string2 = str(input('Please enter a second phrase to concatenate! '))
concatenate = string1 + string2
print(concatenate)
"""
# Exercise thirteen If-Else Statement: Write a program that takes a user's age as input and prints whether they are eligible to vote or not.
"""
loop = 1
while loop == 1:
    print('Hello potential contributor towards the peoples democratic republic of China !!')
    userInput = float(input('Please enter your current age!: '))
    if userInput >= 18:
        print('Congratulations! You are old enough to vote for Xi Jinping! Make the correct decision to vote for our dicta- president Xi Jinping!! \nNext person please! \n')
    elif 0 <= userInput < 18:
        print('Not good!! You are not old enough to vote for Xi Jinping!! Get older fast and try again! \nNext person please! \n')
    elif userInput < 0:
        print('Do not test China !! You will regret it ! Device will now explode!! ')
        loop = 0
"""
# Exercise fourteen Nested If Statements: Implement a program that checks if a number is positive, negative, or zero.
"""
loop = 1
while loop == 1:
    userInput = float(input('Give me a number and I will magically determine whether it is a positive number, a negative number, or a big fat goose egg!! \nEnter number here!: '))
    print('Hmmm....')
    if userInput <= 0:
        print('Well, I can say for certain that the number not positive!')
        if userInput == 0:
            print('Ive got it! The number is definitely a big fat goose egg, just like your big fat head! Loser.')
        else:
            print('Aha!! The number is definitely negative! Just like your terrible personality traits! ')
    else:
        print('I can tell you with utmost confidence that this number is positive! Just like your mothers HIV test!! ')
    print('Thank you for participating. ')
"""
# Exercise fifteen Looping Control Flow: Use a loop to print the numbers from 1 to 10
"""
loop = 1
while loop <= 10:
    print(loop)
    loop = loop + 1
"""