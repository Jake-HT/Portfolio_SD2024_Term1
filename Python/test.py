loop = 1
while loop == 1:
    print('Hello potential contributor to the peoples democratic republic of China !! ')
    userInput = float(input('Please enter your current age!: '))
    if userInput >= 18:
        print('Congratulations! You are old enough to vote for Xi Jinping! Make the correct decision to vote for our dicta- president Xi Jinping \nNext person please! \n')
    elif 0 <= userInput < 18:
        print('Not good!! You are not old enough to vote for Xi Jinping!! Get older fast and try again!! \nNext person please! \n')
    elif userInput < 0:
        print('Do not test China !!! You will have deep regret !! Device will now explode !')
        loop = 0