import os
import shutil

dirPath = r"C:\Users\jaker\Desktop\simple"


def getDate(fileName):
    x = 0
    for char in fileName:
        if char.isdigit():
            break
        else:
            x += 1

    yr = fileName[x:4 + x]
    mo = fileName[4 + x:6 + x]
    da = fileName[6 + x:8 + x]

    return yr, mo, da


def checkValid(yr, mo, da):
    success = False
    if yr.isdigit() and mo.isdigit() and da.isdigit() and 0 < int(mo) < 13 and yr in [str(1900 + z) for z in
                                                                                      range(140)] and 0 <= int(da) < 33:
        success = True
    else:
        success = False
    return success


def filesToMonthFolders(dirPath):
    os.chdir(dirPath)

    months = []
    fileNameList = []

    # check every file to see what months are needed, print some stuff
    for filename in os.listdir():
        if os.path.isfile(filename):
            yr, mo, da = getDate(filename)
            success = checkValid(yr, mo, da)
            if success:
                fileNameList.append(filename)

            if mo not in months and success:
                months.append(mo)

            print('Name: {}, Year: {}, Month: {}, Day: {}.'.format(filename, yr, mo, da))

    # generate folder names based on mo number
    monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthFolderNames = [x + '-' + monthNames[int(x) - 1] for x in months]

    # check to see if month folders already exist
    foldersInDir = []
    for filename in os.listdir():
        if os.path.isdir(filename):
            foldersInDir.append(filename)

    # if a folder is needed, and not already there, create it
    for folderName in monthFolderNames:
        if folderName not in foldersInDir:
            os.mkdir(os.path.join(dirPath, folderName))

    # now move every file to the correct folder
    for filename in fileNameList:
        yr, mo, da = getDate(filename)
        destFolderName = mo + '-' + monthNames[int(mo) - 1]
        destFolderPath = os.path.join(dirPath, destFolderName)
        os.rename(os.path.join(dirPath, filename), os.path.join(destFolderPath, filename))


def filesToYearFolders(dirPath, doMonthsToo=False):
    os.chdir(dirPath)

    years = []
    fileNameList = []

    # check every file to see what months are needed, print some stuff
    for filename in os.listdir():
        if os.path.isfile(filename):
            yr, mo, da = getDate(filename)
            success = checkValid(yr, mo, da)
            if success:
                fileNameList.append(filename)
                if yr not in years:
                    years.append(yr)

            print('Name: {}, Year: {}, Month: {}, Day: {}.'.format(filename, yr, mo, da))

    # check to see if month folders already exist
    foldersInDir = []
    for filename in os.listdir():
        if os.path.isdir(filename):
            foldersInDir.append(filename)

    # if a folder is needed, and not already there, create it
    for folderName in years:
        if folderName not in foldersInDir:
            os.mkdir(os.path.join(dirPath, folderName))

    # now move every file to the correct folder
    for filename in fileNameList:
        yr, mo, da = getDate(filename)
        destFolderName = yr
        destFolderPath = os.path.join(dirPath, destFolderName)
        os.rename(os.path.join(dirPath, filename), os.path.join(destFolderPath, filename))

    # call months sorting on all the year folders
    if doMonthsToo:
        for folderName in years:
            filesToMonthFolders(os.path.join(dirPath, folderName))


print('----Files To Folders by Date Tool - JLaframboise----')
choice = input('Sort to years (1), months (2), or both(3)? ')
choicePath = input("Paste the folder path here: ")
print()

if choice == '1':
    print('Sorting...')
    filesToYearFolders(choicePath)
    print('Completed')
elif choice == '2':
    print('Sorting...')
    filesToMonthFolders(choicePath)
    print('Completed')
elif choice == '3':
    print('Sorting...')
    filesToYearFolders(choicePath, True)
    print('Completed')
else:
    print('Cancelled. ')

# filesToYearFolders(r"C:\Users\jaker\Desktop\fileOrgTesting - Copy")
