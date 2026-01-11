import pathlib 

FILE_PATH = '/'
FOLDER_PATH = '/files/'

def ifFolderExists(foldername):
    folder_path = pathlib.Path(FILE_PATH + foldername)

    if (folder_path.exists()):
        return True
    else:
        return False

def ifFileExists(filename):
    file_path = pathlib.Path(FILE_PATH + filename)

    if (file_path.exists()):
        return True
    else:
        return False
    
def createFolder(foldername):
    print("n")

def createFile(filename):
    if ifFolderExists(filename):
        print(f"A file with the name {filename} already exists. Please chose another name.\n")
    else:
        try:
            open(filename, 'x', encoding=None)
        except: 
            print("An error has occured\n")
    return
    



if __name__ == '__main__':
    print(f"yo yo")