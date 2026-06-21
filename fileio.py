import os
import sys
import csv
import consoleio as cio


'''
MAKE ONE FILE INSTEAD OF MULTIPLE NOT NECESSARY
'''

FOLDER = os.getcwd() + '/files'
FILEPATH = os.getcwd() + '/files/media.csv'

#def fileStorage

def unexpectedErrorMessage(Exception):
    print(f"A unexpected error has occured: {Exception}")

def doesFileExist(filename):
    filepath = FOLDER + '/' + filename

    if not os.path.isfile(filepath):
        createFile(filename)
    else:
        pass

    
# File creation/deletion functions
def createFile(filename):

    file_path = os.path.join(FOLDER, filename)

    try:
        open(file_path, 'x', encoding=None)
        print(f'{filename} has successfully been created')
    except FileExistsError: 
        print(f"\nFile with the name {filename} already exists")
    except Exception:
        unexpectedErrorMessage(Exception)
        
    return


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


def resetFiles():
    pass


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

def addEntry():

    function_marker = [False, False]

    print('Name: ', end='')
    media_name = input()
    #print('\n')

    print('Medium: ', end='')
    media_medium = input()
    
    print('Category: ', end='')
    media_category = input()

    print('Description: ', end='')
    media_description = input()

    media_complete = None

    while true:
        print('Complete: ')
        print('1. Yes')
        print('2. No')
        media_complete = inputLine()
        if media_complete != 1 or media_complete != 2:
            print("please enter either 1 or 2 to indicate if the media has been completed")
        else:
            break

    print('Rating: ', end='')
    media_rating = input()

    print('Rating Scale: ', end='')
    media_rating_scale = input()

    print('Comments: ', end='')
    media_comments = input()

    if media_rateing is '':
        function_marker[0] = True
    
    if media_rating_scale is '':
        function_marker[1] = True

    curr_entry = None

    if function_marker[0] == False and function_marker[1] == False:
        curr_entry =  md(media_name, media_medium, media_category, media_description, media_comments)
    elif function_marker[0] == True and function_marker[1] == True:
        curr_entry =  md(media_name, media_medium, media_category, media_description, media_comments, media_rating, media_rating_scale)
    elif function_marker[0] == False and function_marker[1] == True:
        curr_entry =  md(media_name, media_medium, media_category, media_description, media_comments, rating_scale=media_rating_scale)
    elif function_marker[0] == True and function_marker[1] == False:
        curr_entry =  md(media_name, media_medium, media_category, media_description, media_comments, rating=media_rating)
    
    

def editEntry():

    pass

def delete_entry():

    pass

if __name__ == '__main__':
    print(f"yo yo")