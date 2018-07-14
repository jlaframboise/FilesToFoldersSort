import os


def dumpSubFoldersToParent(path):
    os.chdir(path)
    print('Running from {}'.format(path))

    #ogListDir = os.listdir()
    for x in os.listdir():

        if os.path.isdir(x):
            dumpSubFoldersToParent(os.path.join(path,x))
            os.chdir(path)
            print('Back in {}'.format(path))

    for x in os.listdir():
        if os.path.isfile(x):
            filePath = os.path.join(path, x)
            destPath = os.path.join(os.path.split(path)[0], x)
            print('Moving: {} to {}'.format(filePath, destPath))
            os.rename(filePath, destPath)


def dumpSubFoldersToSelf(path):
    os.chdir(path)
    for x in os.listdir():
        if os.path.isdir(x):
            dumpSubFoldersToParent(os.path.join(path, x))
            os.chdir(path)

#testPath = r"C:\Users\jaker\Desktop\fileOrgTesting - Copy"

print('----Dissolve Folders Tool - JLaframboise----')
choice = input('Dissolve inside self(1), or up to parent(2)? ')
choicePath = input("Paste the folder path here: ")
print()

if choice == '1':
    print('Dissolving...')
    dumpSubFoldersToSelf(choicePath)
    print('Completed')
elif choice == '2':
    print('Dissolving...')
    dumpSubFoldersToParent(choicePath)
    print('Completed')
else:
    print('Cancelled. ')