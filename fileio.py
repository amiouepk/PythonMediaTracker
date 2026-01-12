import os

FOLDER = 'files'

#def fileStorage

def unexpectedErrorMessage(Exception):
    print(f"A unexpected error has occured: {Exception}")
    
def createFolder(foldername):
    print("n")

def createFile(filename):

    file_path = os.path.join(FOLDER, filename + '.csv')
    try:
        open(file_path, 'x', encoding=None)
    except FileExistsError: 
        print(f"\nFile with the name {filename} already exists")
    except Exception:
        unexpectedErrorMessage(Exception)
        
    return

def renameFile(currentfilename, newfilename):

    currentfilename = os.path.join()

    try: 
        os.rename(currentfilename, newfilename)
    except FileNotFoundError:
        print(f'File by the name of {currentfilename} does not exist.\n')
    except FileExistsError:
        print(f'File by the name of {newfilename} already exists.\n')
    except Exception:
        unexpectedErrorMessage(Exception)

    return

    



if __name__ == '__main__':
    print(f"yo yo")