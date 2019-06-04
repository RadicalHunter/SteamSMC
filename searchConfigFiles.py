import os
import pathlib
import stat
import time
import datetime


'''
Locate drive(s) Up

'''
driveLetterList = ['A:','D:','C:','B:','E:','F:','G:','H:','I:','J:','K:','L:','M:','N:','O:','P:','Q:','R:','S:','T:','U:','V:','W:','X:','Y:','Z:']


def findDrive(self):
    existingDrives = []
    nbDrives = 0
    for letter in self:
        try:
            # print(letter)
            value = pathlib.Path(letter)
            # print(value.exists())
            if value.exists() == True:
                existingDrives.append(letter)
                nbDrives = nbDrives + 1
        except WindowsError:
            # print('Permission Denied for ' + letter)
            pass

    # print('We found {0} drive(s) up {1}'.format(nbDrives, existingDrives))
    return existingDrives

drives = findDrive(driveLetterList)

'''
Search steamapps folder
'''

def locateSteamFolder(self):
    # NB: Ajouter dans un tableau la valeur de existingPath a chaque boucle si a la fin le table ne contient que false alors demander à l'utilisateur de rentrer le path en input
    for letter in self:
        path = letter + '\\Program Files (x86)\\Steam\\userdata'
        existingPath = pathlib.Path(path).exists()
        if existingPath == True:
            return path


steamPath = locateSteamFolder(drives)
print(steamPath)

'''
trouve les profils présent et regarde si le fichier de conf et présent

NB: Séparer les deux actions en deux fonction ?
Ajouter un dictionnaire contenant le nom et le path du fichier de conf
'''

def findUserFolder ():
    finalDic = {}
    for x in os.listdir(steamPath):
        exists = os.path.isfile(steamPath + '\\' + x + '\\730\\local\\cfg\\config.cfg')
        if exists:
            configFilePath = steamPath + '\\' + x + '\\730\\local\\cfg\\config.cfg'

            # Get file's Last modification time stamp only in terms of seconds since epoch
            modTimesinceEpoc = os.path.getmtime(configFilePath)
            # Convert seconds since epoch to readable timestamp
            modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
            # print('config file found on profile folder ' + x)
            openConfigFile = open(configFilePath,'r',
                                    encoding='utf8')
            readConfigFile = openConfigFile.read()
            splited_config = readConfigFile.split("\n")
            # print(splited_config)
            for lines in splited_config:
                values = lines.split(' ')
                # print(values)
                if 'name' in values:
                    values.remove('name')
                    cleanValues = " ".join(values)
                    dic = {'name':cleanValues.replace('"',''),'path':configFilePath,'folder':x,'update':modificationTime}
                    finalDic[x] = dic
                    print('We found settings of ' + cleanValues + ' account from ' + x + ' Last modified at : ' + modificationTime)
                    openConfigFile.close()
                else:
                    pass
        else:
            print('No config file on profile folder ' + x)
            pass
    print(finalDic)

findUserFolder()