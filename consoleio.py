#General Functions
def inputLine():

    print("Enter: ", end = '')
    input_str = input()

    return input_str

def helpMessage():
    print(f"Help message\n")

    return

def inputErrorMessage():
    print(f"")

    return

def incorrectOptionErrorMessage():
    print(f"\nPlease enter one of the numbers listed")


#main.py output functions
def initialMessage():

    print(f"Options:\n")
    print(f"0. Exit\n")
    print(f"1. Add Entry\n")
    print(f"3. Category Options\n")
    print(f"4. Help\n")

    return

def addEditOptionsMessage():
    pass
        
def categoryOptions():
    print(f"Options:\n")
    print(f"0. Previous Menu\n")
    print(f"1. Edit Category\n")
    print(f"2. Add Category\n")
#mediaData.py Output Options



# date.py Class Options
def changeDateOptions():
    print("Options: ")
    print("0. Previous Menu")
    print("1. All")
    print("2. Year")
    print("3. Month")
    print("4. Day")
    print("Typically you can remember the year first, and than the month, and then the day")

def changeDayOptions():
    print("Enter the desired date: ")





if __name__ == "__main__":

    print("huh")