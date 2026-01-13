import consoleio as cio
import fileio as fio

# Change files options to category options with each file corresponding to a category


filename = 'text.txt'

def editFiles():
    cio.editFilesOptionsMessage()

def fileOptions():

    while 1:
        cio.fileOptionsMessage()
        file_options_input = cio.inputLine()

        match file_options_input:
            case '1': #Create Default files
                fio.createFile('movies')
                fio.createFile('books')
                fio.createFile('tvshows')
                fio.createFile('games')
                #fio.createFile('')
                
            case '2': #Create Custom Files

                while 1:
                    print('Enter Desired File Name: ', end = '')
                    filename = input()
                    fio.createFile(filename)

                    while 1:
                        print('Would you like to create another file?')
                        print('1. Yes\n')
                        print('2. No\n')
                        print('Enter: ', end = '')
                        createCustomFileInput = input()

                        match createCustomFileInput:
                            case '1':
                                break
                            case '2':
                                break
                            case _:
                                cio.incorrectOptionErrorMessage()
                                continue

                    if createCustomFileInput is '2':
                        break

            case '3': #Delete File
                while 1:
                    print('Enter Desired File Name: ', end = '')
                    filename = input()
                    fio.deleteFile(filename)
                    break


            case '4': #Edit File Name
                print('Enter Current File Name: ', end = '')
                currentfilename = input()
                
                print('Enter New File Name: ', end = '')
                newfilename = input()

                fio.renameFile(currentfilename, newfilename)
            case '5': #Previous Menu
                return
            case '6':
                print("place holder\n")
            case '_':
                print("place holder\n")

def testFiles():

    while 1 == 1:
        cio.testOptionsMessage()
        str_input = cio.inputLine()

        match str_input:
            case 1: #Create Default Files
                print("place holder\n")
            case 2: #Create Custom Files
                print("place holder\n")
            case 3: #Edit File Name
                print("place holder\n")
            case 4: #Previous Menu
                print("place holder\n")
            case '_':
                print("place holder\n")
            
def intitalOptions():

    print(f"-----------------Welcome-----------------")

    while 1 == 1:
        cio.initialMessage()
        initial_opt_input = cio.inputLine()


        match initial_opt_input:
            case '1': # Add/Edit
                editFiles()
            case '2': # File options
                fileOptions()
            case '3': #Test Options
                testFiles()
            case '4': #Files
                cio.helpMessage()
            case '5': #Exit
                exit(0)
            case _: #Error Message
                cio.incorrectOptionErrorMessage()
                


if __name__ == "__main__":
    
    intitalOptions()

    #print("huh\n")
    
