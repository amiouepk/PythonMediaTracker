import os
import consoleio as cio

'''
MAKE ONE FILE INSTEAD OF MULTIPLE NOT NECESSARY
'''



FOLDER = 'files'

#def fileStorage

def unexpectedErrorMessage(Exception):
    print(f"A unexpected error has occured: {Exception}")
    
# File creation/deletion functions
def createFile(filename):

    file_path = os.path.join(FOLDER, filename + '.csv')

    try:
        open(file_path, 'x', encoding=None)
        print(f'{filename} has successfully been created')
    except FileExistsError: 
        print(f"\nFile with the name {filename} already exists")
    except Exception:
        unexpectedErrorMessage(Exception)
        
    return

def createDefaultFiles():
    
    createFile('movies')
    createFile('books')
    createFile('tvshows')
    createFile('games')

def renameFile(currentfilename, newfilename):

    currentfilenamePath = os.path.join(FOLDER, currentfilename + '.csv')
    newfilenamePath = os.path.join(FOLDER, newfilename + '.csv')

    try: 
        os.rename(currentfilenamePath, newfilenamePath)
        print(f'{currentfilename} has been successfully changed to {newfilename}\n')
    except FileNotFoundError:
        print(f'File by the name of {currentfilenamePath} does not exist.\n')
    except FileExistsError:
        print(f'File by the name of {newfilenamePath} already exists.\n')
    except Exception:
        unexpectedErrorMessage(Exception)

    return



def deleteFile(filename):

    file_path = os.path.join(FOLDER, filename + '.csv')

    try:
        os.remove(file_path)
        print(f"file {filename + '.csv'} has been successfully deleted")
    except FileNotFoundError:
        print(f"\nFile with the name {filename} does not exists")
    except PermissionError:
        print(f"You do not have permission to delete {filename}")
    except Exception:
        unexpectedErrorMessage()
    
    return
        
# File modification funcitons

def add_entry():

    pass

def edit_entry():

    pass

def delete_entry():

    pass

if __name__ == '__main__':
    print(f"yo yo")