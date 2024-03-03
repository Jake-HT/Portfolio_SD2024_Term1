# REQUIREMENTS!!! 
# Add New Vendor Details: Onboard new vendors, their contact details must be easily added to the system. This includes their name (or company name), phone number, and email address.

# Access Vendor Information Quickly: For ongoing projects, team members must quickly access specific vendor details with a simple search.

# Remove Vendors: If a vendor goes out of business or if there's a decision to cease collaboration due to quality issues, their details must be swiftly removed from the system.

# Update Vendors: Vendor details must be able to be updated to provide relevant updated information.

# Add Extra Vendor Details: Give the ability for the users to add extra details they may need from Vendors (e.g. Vendor categories)

# Simple Menu: Add a simple terminal menu that allows you to select which operations you want to perform when using the application.
class Vendors: # Declares Vendor class
    def __init__(self): # initialises vendor dictionary with keys as string and values as list
        self.Vendors = dict({
            "SouljaBoy" : ["6789998212","soulja.boy@tellemail.net"],
            "W3Schools": ["1 <3 U","myrobotwife@mybeloved.com"],
            "Hog Rider": ["312213","alwaysbreaksthrough@infinitedamage.com","Impossible to defend"]
        })
        pass

    def SearchVendors(self): # declares SearchVendors function
        resultCounter = 0 # initialises a result counter as 0 
        userInput = str(input("---------------------\nPlease enter your search query!: ")) # takes user input to search vendors
        for key, value in self.Vendors.items(): # iterates through dictionary keys and values
            if key == userInput: # checks if user's search query matches any dictionary key
                resultCounter += 1 # Adds 1 to the result counter to prevent resultCounter == 0 from activating
                print(f"Vendor '{key}' found! \nDisplaying information!:") 
                if value.__len__() == 2: # checks if the dictionary list has 2 values, being the phone number and email, and prints results accordingly
                    print(f"Vendor Phone Number: {value[0]} \nVendor Email Address: {value[1]}") 
                    pass
                elif value.__len__() == 3: # checks if the dictionary list has 3 values, being phone number, email and extra details and prints results accordingly
                    print(f"Vendor Phone Number: {value[0]} \nVendor Email Address: {value[1]} \nExtra details: {value[2]}")
                    pass
            pass
        if resultCounter == 0: # if no results were found during the search, resultCounter will remain at 0 and prints appropriate response
            print(f"No Vendors found matching {userInput}...")
            pass
        pass

    def AddVendors(self): # declares AddVendors function
        print("---------------------\nAdding new Vendor! \n---------------------")
        key = str(input("What is the name of the Vendor/ Vendor Company?: ")) # takes user input for the vendor name, acting as the key in the dictionary item 
        valuesList = list([str(input("What is the Vendor/ Vendor Company's contact number?: ")),str(input("What is the Vendor/ Vendor Company's email address?: "))]) # takes two inputs as vendor phone number and email, and adds to a list
        self.Vendors[key] = valuesList # Adds new key and value to dictionary using the previous inputs
        pass

    def UpdateVendors(self): # declares UpdateVendors function
        resultCounter = 0 # initialises a result counter as 0
        userInput = str(input("---------------------\nPlease enter your search query!: ")) # takes user input to search for existing vendors
        for key, value in self.Vendors.items(): # iterates through dictionary keys and values
            if key == userInput: # checks if user's search query matches any dictionary key
                resultCounter += 1 # Adds 1 to the result counter to prevent resultCounter == 0 from activating
                print(f"Vendor '{key}' found! \nDisplaying current details!:") # if a result is found, prints appropriate result
                if value.__len__() == 2: # checks if the dictionary list has 2 values, being the phone number and email, and prints results accordingly
                    print(f"Vendor Phone Number: {value[0]} \nVendor Email Address: {value[1]}") 
                    valuesList = list([str(input("What is the Vendor/ Vendor Company's new contact number?: ")),str(input("What is the Vendor/ Vendor Company's new email address?: "))]) # takes two inputs as vendor phone number and email, and adds to a list
                    self.Vendors[key] = valuesList # Adds updated values using the previous inputs to the relevant dictionary key
                    pass
                elif value.__len__() == 3: # checks if the dictionary list has 3 values, being phone number, email and extra details and prints results accordingly
                    print(f"Vendor Phone Number: {value[0]} \nVendor Email Address: {value[1]} \nExtra details: {value[2]}")
                    valuesList = list([str(input("What is the Vendor/ Vendor Company's new contact number?: ")),str(input("What is the Vendor/ Vendor Company's new email address?: ")),str(input("What is the Vendor/ Vendor Company's extra details?"))]) # takes three inputs as vendor phone number, email and extra details, and adds to a list
                    self.Vendors[key] = valuesList # Adds updated values using the previous inputs to the relevant dictionary key
                    pass
            pass
        if resultCounter == 0: # if no results were found during the search, resultCounter will remain at 0 and prints appropriate response
            print(f"No Vendors found matching {userInput}...")
            pass
        pass

    def AddVendorDetails(self):
        resultCounter = 0 # initialises a result counter as 0
        userInput = str(input("---------------------\nPlease enter your search query!: ")) # takes user input to search for existing vendors
        for key, value in self.Vendors.items(): # iterates through dictionary keys and values
            if key == userInput: # checks if user's search query matches any dictionary key
                resultCounter += 1 # Adds 1 to the result counter to prevent resultCounter == 0 from activating
                if value.__len__() == 2: # checks if the dictionary list has 2 values, being the phone number and email
                    print(f"Vendor '{key}' found!")
                    userInput = str(input("What detail would you like to add to this Vendor?: ")) # takes extra detail as user input
                    value.append(userInput) # appends extra detail to the dictionary value of relevant key
                    pass
                elif value.__len__() == 3: # checks if the dictionary list has 3 values, being phone number, email and extra details
                    print(f"Vendor '{key}' found! \nVendor already has extra details. Please go to Update Vendor Details instead!") # if extra detail already exists, prompts user to update details instead.
                    pass
            pass
        if resultCounter == 0: # if no results were found during the search, resultCounter will remain at 0 and prints appropriate response
            print(f"No Vendors found matching {userInput}...")
            pass
        pass

    def RemoveVendors(self):
        resultCounter = 0 # initialises a result counter as 0
        userInput = str(input("---------------------\nPlease enter the name of the Vendor you'd like to remove: ")) # takes user input to search for existing vendors
        for key in self.Vendors.keys(): # iterates through dictionary keys
            if key == userInput: # checks if user's search query matches any dictionary key
                resultCounter += 1 # Adds 1 to the result counter to prevent resultCounter == 0 from activating
            pass
        if resultCounter == 1: # If a result is found, deletes relevant dictionary item
                print(f"Vendor '{key}' found! \nRemoving now!...")
                self.Vendors.pop(userInput)        
                pass
        elif resultCounter == 0: # if no results were found during the search, resultCounter will remain at 0 and prints appropriate response
            print(f"No Vendors found matching {userInput}...")
            pass
        pass
    
    pass

programRunning = True # declared variable 'programRunning' as True boolean to detemine whether the following while loop containing the program menu will run
stellarEventsVendors = Vendors() # summons object of Vendor class

while programRunning == True:
    print("---------------------\nWelcome to the StellarEvents Contact Book! \n---------------------\nWhich operation would you like to perform?: "+
        "\n1. Search Vendor Information \n2. Add New Vendor Details\n3. Update Vendor Details "+
        "\n4. Add Extra Vendor Details \n5. Remove Vendor \n6. Close the program")
    userInput = str(input("Please input the corresponding number!: ")) # userInput is declared as string input despite taking numeric values to avoid program breaking if incorrect input is used
    if userInput == '1': # handles 'Search Vendor Information' operation
        stellarEventsVendors.SearchVendors()
        pass
    elif userInput == '2': # handles 'Add New Vendor Details' operation
        stellarEventsVendors.AddVendors()
        pass
    elif userInput == '3': # handles 'Update Vendor Details' operation
        stellarEventsVendors.UpdateVendors()
        pass
    elif userInput == '4': # handles 'Add Extra Vendor Details' operation
        stellarEventsVendors.AddVendorDetails()
        pass
    elif userInput == '5': # handles 'Remove Vendor' operation
        stellarEventsVendors.RemoveVendors()
        pass
    elif userInput == '6': # handles 'Close the program' operation
        print("---------------------\nThank you for using StellarEvents Contact Book! \nClosing program now!...")
        programRunning = False # variable 'programRunning' which controls the while loop contianing the program updates to false, ending the program.
        pass
    else: # handles any other incorrecct inputs and prompts user to try again.
        print("Invalid input!!! Please try again with a valid response!")
        pass