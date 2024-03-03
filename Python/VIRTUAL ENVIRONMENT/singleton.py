# declaring class name as PirateKing 
class PirateKing:

    # declaring _insance variable as None, indicates whether the class object has been summoned before
    _instance = None

    # class variable that stores the pirate king's name 
    _king = None

    # uses __new__ method which triggers automatically when the class is created. cls is the self keyword, and userInput is a userInput I used for testing
    def __new__(cls,userInput):

        # checking if the instance has not been summoned before
        if cls._instance == None:

            # if no instance is found, creates instance of PirateKing using the super() function
            cls._instance = super(PirateKing, cls).__new__(cls)

            # assigns value of userInput to _king, declaring *x* as king of the pirates.
            cls._king = userInput

        # returns the new or existing instance of the Pirate King
        return cls._instance
    
    # defines function findTreasure for finding treasures, self is self keyword and treasureName is the user input
    def findTreasure(self, treasureName):

        # function returns print statement, displaying that *pirate king* has found *treasure*
        print(f"{self._king} found the {treasureName}!!")

    pass

# summons class object of PirateKing as variable ZohebKhan, with name parameter "Zoheb Khan"
ZohebKhan = PirateKing("Zoheb Khan")

# summons class object of PirateKing as variable RichardSingh, with name parameter "Richard Singh"
RichardSingh = PirateKing("Richard Singh")

# Zoheb tries to find a treasure titled "One Piece"
ZohebKhan.findTreasure("One Piece")

# Richard tries to find a treasure titled "Zoheb Pole Dance"
RichardSingh.findTreasure("Zoheb Pole Dance")