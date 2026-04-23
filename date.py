import consoleio as cio
from datetime import datetime


class date:

    # 0 = Not added/Assumed not available.
    # month goes up till 12 (december)
    # day does up until 31/30/28/29 depending on the month
    # years whatever

    US = True #US date or rest of world date

    def __init__(self, year = 0, month = 0, day = 0):
        self.day = day
        self.month = month
        self.year = year

    def changeDay(self, day):
        self.day = day
    
    def changeMonth(self, month):
        self.month = month
    
    def changeYear(self, year):
        self.year = year

    def changeDate(self, year, month, day):
        cio.changeDateOptions()
        changeDateInputOption = cio.inputLine()

        while 1:

            match changeDateInputOption:
                case '0': 
                    return
                case '1':
                    date.changeDay()
                case '2':
                    date.changeMonth()
                case '3':
                    date.changeYear()
                case _:
                    cio.incorrectOptionErrorMessage()
                    continue





    def printDate (self):
        
        if self.day is 0 and self.month is 0:
            print(f"{self.year}")
        elif self.day is 0:
            print(f"{self.month}/{self.year}")
        else:
            if date.US is True:
                print(f"{self.month}/{self.day}/{self.year}")
            else:
                print(f"{self.day}/{self.month}/{self.year}")
        



if __name__ == '__main__':


    print()



