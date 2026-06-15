import consoleio as cio
import fileio as fio

# Change files options to category options with each file corresponding to a category


media_file = 'media.csv'
category_file = 'categories.csv'

def editFiles():

    while True:
        cio.editFilesOptionsMessage()
        str_input = cio.inputLine()

        # match str_input:
        #     case '1':

def categoryOptions():
    while True:
        cio.categoryOptions()
        cat_opt_input = cio.inputLine()

        match cat_opt_input:
            case '0': #Previous Menu
                break
            case '1': #Edit Existing Category
                pass
            case '2': #Add New Category
                pass
        

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
                add()
            case '2': # Add/Edit Category
                categoryOptions()
            case '3': # Reset
                ()
            case _: #Error Message
                cio.incorrectOptionErrorMessage()
                


if __name__ == "__main__":
    
    intitalOptions()

    #print("huh\n")
    
