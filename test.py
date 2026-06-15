import os




folderpath = os.getcwd()
filepath = folderpath + '/main.py'

print(f"Does main.py exist?")
print(filepath)
print(os.path.isfile(filepath))

afp = folderpath + '/files/media.csv'

print(f"Does media.csv exist?")
print(afp)
print(os.path.isfile(afp))

