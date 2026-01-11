import print_messages as pm
import fileio as fio

filename = 'text.txt'

def editFiles():
    pm.editFilesOptionsMessage()

def fileOptions():

    while 1 == 1:
        pm.fileOptionsMessage()
        str_input = pm.inputLine()

        match str_input:
            case 1:
                fio.createFile('movies.csv')
                fio.createFile('books.csv')
                fio.createFile('tvshows.csv')
                fio.createFile('games.csv')
                #fio.createFile('')
            case 2:
                print('Enter File Name: ')
                filename = input()
                fio.createFile(filename)
            case 3:
                print("place holder\n")
            case 4:
                return
            case 5:
                print("place holder\n")
            case '_':
                print("place holder\n")

        #print("\n\n")

def testFiles():

    while 1 == 1:
        pm.testOptionsMessage()
        str_input = pm.inputLine()

        match str_input:
            case 1: #Create Default Files
                print("place holder\n")
            case 2: #Create Custome Files
                print("place holder\n")
            case 4:
                print("place holder\n")
            case 5:
                print("place holder\n")
            case '_':
                print("place holder\n")
            
def intitalOptions():

    print(f"-----------------Welcome-----------------")

    while 1 == 1:
        pm.initialMessage()
        str_input = pm.inputLine()


        match str_input:
            case 1:
                editFiles()
            case 2:
                fileOptions()
            case 3:
                testFiles()
            case 4:
                pm.helpMessage()
            case 5:
                exit()
            case '_':
                pm.editFilesOptionsMessage()
                







if __name__ == "__main__":

    intitalOptions()

    print("huh\n")
    
