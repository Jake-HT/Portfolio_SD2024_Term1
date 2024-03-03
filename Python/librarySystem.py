def recordsAdd(title, author, genre):
    recordsTitle.append(title)
    recordsAuthor.append(author)
    recordsGenre.append(genre)
    recordsID.append(int(len(recordsID)))

def recordsDisplay():
    for i in recordsID:
        print("Book title is: {0} | Book author is: {1} | Book genre is: {2} | Book ID is: {3}".format(recordsTitle[i], recordsAuthor[i], recordsGenre[i], recordsID[i]))

def recordsSearch(title):
    for i in recordsID:
        if title in recordsTitle[i]:
            print("Book with matching title found! Author is {0}, the genre is {1}, and the ID is {2}".format(recordsAuthor[i], recordsGenre[i], recordsID[i]))
        
recordsTitle = ["Fairy Tail", "One Piece", "Attack on Titan", "Jojo's Bizarre Adventure"]
recordsAuthor = ["Hiro Mashima", "Eiichiro Oda", "Hajime Isayama", "Hirohiko Araki"]
recordsGenre = ["Adventure", "Adventure", "Thriller", "Adventure"]
recordsID = [0, 1, 2, 3]

loop = 1
while loop == 1:
    userInput = input("Welcome to the Library! \nInput 1 to add a new book to the Library Records! \nInput 2 to display all books currently registered in our Library Records! \nInput 3 to search for a book in the Library Record via the title! \nOr input 0 to close the program! \n")
    if userInput == '1':
        inputTitle = str(input("Adding new book to Library Records! \nWhat is the Title of the book?: "))
        inputAuthor = str(input("Who is the Author of the book?: "))
        inputGenre = str(input("What is the Genre of the book?: "))
        recordsAdd(inputTitle, inputAuthor, inputGenre)

    elif userInput == '2':
        recordsDisplay()
    
    elif userInput == '3':
        inputSearch = str(input("What is the title of the book?: "))
        recordsSearch(inputSearch)
    
    elif userInput == '0':
        print("Thank you for using the Library Records system! \nProgram will now close...")
        loop = 0

    else:
        print("Invalid input. Please try again")