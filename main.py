import consoleio as cio
import fileio as fio
import mediadata as md

# Change files options to category options with each file corresponding to a category


media_file = 'media.csv'
category_file = 'categories.csv'

def addEditOptions():

    while True:
        cio.addEditOptionsMessage()
        str_input = cio.inputLine()

        match str_input:
            case '0':
                break
            case '1':
                fio.addEntry()
            case '2': #Edit Existing Category
                fio.editEntry()
            case '3': #List #x of entries
                pass
            case '4': #List all entries
                pass

def categoryOptions():
    while True:
        cio.categoryOptions()
        cat_opt_input = cio.inputLine()

        match cat_opt_input:
            case '0': #Previous Menu
                break
            case '1': #Add New Category          
                fio.addCategory()
            
                
        # try:
        #     open(FOLDER + '/media.csv', 'w+')
        #     cio.categoryOptions()
        #     cat_opt_input = cio.inputLine()

            

        # except FileNotFoundError:
        #     print(f'File by the name of {'media.csv'} does not exist.\n')
        # except Exception:
        #     unexpectedErrorMessage(Exception)

        
        

    pass


            
def intitalOptions():

    fio.doesFileExist('media.csv')
    fio.doesFileExist('categories.csv')

    print(f"-----------------Welcome-----------------")

    while True:
        cio.initialMessage()
        initial_opt_input = cio.inputLine()


        match initial_opt_input:
            case '0': #Exit
                exit(0)
            case '1': # Add/Edit Media
                addEditOptions()
            case '2': # Add/Edit Category
                categoryOptions()
            case '3': # Reset
                ()
            case _: #Error Message
                cio.incorrectOptionErrorMessage()
                


if __name__ == "__main__":
    
    intitalOptions()

    #print("huh\n")
    
