import print_messages as pm



def editFiles():
    pm.editFilesOptionsMessage()

def fileOptions():
    pm.fileOptionsMessage()

def testFiles():
    pm.testOptionsMessage()


def intitalOptions():

    pm.initialMessage
    #pm.inp
    str_input = ''

    while 1 is 1:
        match pm.inputLine(str_input):
            case '1':
                editFiles()
            case '2':
                fileOptions()
            case '3':
                testFiles()
            case '4':
                pm.helpMessage()
            case '5':
                exit()
            case '_':
                







if __name__ == "__main__":

    print("huh\n")
    
