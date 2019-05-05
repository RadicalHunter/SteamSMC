import os
import pathlib

disk =''
path = disk + ':/'
config = 'config.cfg'

openConfigFile = open('E:\\Program Files (x86)\\Steam\\userdata\\72453270\\730\\local\\cfg\\config.cfg', 'r', encoding='utf8')

finalPath = ''

# print(os.environ['SystemDrive'])
# print(pathlib.WindowsPath('\\'))

driveLetterList = ['A:','D:','B:','E:','F:','G:','H:','I:','J:','K:','L:','M:','N:','O:','P:','Q:','R:','S:','T:','U:','V:','W:','X:','Y:','Z:']
existingDrives = []

for letter in driveLetterList:
    try:
        print(letter)
        value = pathlib.Path(letter)
        print(value.exists())
        if value.exists() == True:
            existingDrives.append(letter)
    except WindowsError:
        print('Permission Denied')

print(existingDrives)

for letter in existingDrives:
    openConfigFile = open(letter + '\\Program Files (x86)\\Steam\\userdata\\72453270\\730\\local\\cfg\\config.cfg', 'r',
                          encoding='utf8')
    readConfigFile = openConfigFile.read()
    splited_config = readConfigFile.split("\n")
    for lines in splited_config:
        configDict = {}
        values = lines.split(' ')
        if len(values) == 2 and values[0] == 'name':
            print(values[1].replace('"', ""))

    print(configDict)