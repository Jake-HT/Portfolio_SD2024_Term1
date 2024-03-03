# Exercise one Input Prompt: Write a program that takes the user's name as input and prints a personalized greeting.
def userGreeting():
    userInput = input("Hi, what is your name? \n")
    print("What's up, " + userInput + "! Hope you have a good day!")

# Exercise two Numeric Input: Create a program that asks the user to enter two numbers and calculates their sum.
def sumCalculator():
    x = input("Enter a first number!: ")
    y = input("Enter a second number!: ")
    sum = x + y
    print("The sum of these two numbers is " + sum + "!")

# Exercise three Favorite Color: Prompt the user to enter their favorite color and display a message acknowledging their choice.
def favouriteColour():
    userInput = input("Hi, what is your favourite colour? \n")
    print("So " + userInput + "is your favourite colour? Mine too!")

# Exercise four Print Multiple Lines: Write a program that prints a message on one line, and then on the next line, prints a different message.
def multipleLines():
    print("Good morning!... \n*Ten and a half hours later* \nGood night!...")

# Exercise five Formatted Output: Create a program that prints a sentence with placeholders for the user's name and age.
def formattedOutput(name, age):
    if len(age) == 0:
        age = 'agePlaceholder'
    if len(name) == 0:
        name = 'namePlaceholder'
    text = "How did you live to {ageOutput} years old with a name like {nameOutput}?!!"
    print(text.format(ageOutput = age, nameOutput = name))

name = ''
age = ''
# formattedOutput(name, age)

# Exercise six Repeated Output: Print the message "Hello" five times using a loop.
def repeatedOutput():
    userInput = input("Hi, I will say Hello as many times as you'd like me to. How many times would you like me to say Hello? \n")
    if type(userInput) == str:
        print("That is not a number... I will not speak to you.")
    else:
        while userInput > 0:
            print("Hello!")
            userInput = userInput - 1

# Exercise seven Variable Swap: Swap the values of two variables and print the result.
def swapVariables():
    var1 = input("Input a value to assign to variable one!: ")
    var2 = input("Input a value to assign to variable two!: ")
    print("I will swap variables {x} and {y}! ".format(x = var1, y = var2))
    var1, var2 = var2, var1
    print("Values have been swapped to {x} and {y}! ".format(x = var1, y = var2))

# Exercise eight Variable Concatenation: Concatenate two strings stored in variables and print the combined string.
def variableMarriage():
    string1 = input("Input some text to marry to the second piece of text!: ")
    string2 = input("Input some text to marry to the first piece of text!: ")
    print("I hereby pronounce you, " + string1 + string2 + "!! ")

# Exercise nine Variable Initialization: Declare a variable to store your age and initialize it with your actual age.
def variableInitiation(var):
    var = input("Please enter your age!: ")
    return var

var = float()

# Exercise ten Arithmetic Operations: Write a program that takes two numbers as input and performs addition, subtraction, multiplication, and division.
def mathStuff():
    x = float(input("Enter a first number!: "))
    y = float(input("Enter a second number!: "))
    print("Addition: {0} \nSubtraction: {1} \nMultiplication: {2} \nMultiplication: {3}".format(x + y, x - y, x / y, x * y))

# Exercise eleven Comparison Operators: Create a program that compares two numbers and prints whether they are equal or not.
def equalityIsntReal():
    x = input("Enter a first variable!: ")
    y = input("Enter a second variable!: ")
    if x == y:
        print("The variables appear to be equal.")
    elif x != y:
        print("The variables appear to be inequal.")
    else:
        print("What...?")

# Exercise twelve String Concatenation: Concatenate two strings and print the result.
def variableMarriage_Again():
    string1 = input("Input some text to marry to the second piece of text!: ")
    string2 = input("Input some text to marry to the first piece of text!: ")
    print("I hereby pronounce you, " + string1 + string2 + "!! ")

# Exercise thirteen If-Else Statement: Write a program that takes a user's age as input and prints whether they are eligible to vote or not.
def votingAge():
    userInput = float(input("How old are you currently?: "))
    if userInput >= 18:
        print("Congratulations! You are old enough to vote!!")
    elif 0 < userInput < 18:
        print("You are not old enough to vote yet...")
    else:
        print("You aren't even born yet...??? ")

# Exercise fourteen Nested If Statements: Implement a program that checks if a number is positive, negative, or zero.
def numeratorPosNegZero():
    userInput = float(input("I am the Akin- the Numerator!! \nGive me a number and I will tell you if it is positive, negative or zero!: "))
    if userInput >= 0:
        print("The number is DEFINITELY not negative....")
        if userInput != 0:
            print("I've got it!! The number must be positive! ")
        else:
            print("The number is most certainly zero! ")
    else:
        print("This number is negative!")

# Exercise fifteen Looping Control Flow: Use a loop to print the numbers from 1 to 10
def numberPrintLoop():
    i = int(input("I will count down from whichever number you provide me. Please provide a number: "))
    while i > 0:
        print(i)
        i = i - 1