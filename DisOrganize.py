import os

'''
def unsortTree(path):
    os.chdir(path)

    for x in os.listdir():
        if os.path.isdir(x):
            unsortTree(os.path.join(path, x))
            pass
    for x in os.listdir():
        if os.path.isfile(x):
            filePath = os.path.join(path, x)
            destPath = os.path.join(os.path.split(path)[0], x)
            os.rename(filePath, destPath)
'''

def unsortTree(path):
    os.chdir(path)
    print('Running from {}'.format(path))

    #ogListDir = os.listdir()
    for x in os.listdir():

        if os.path.isdir(x):
            unsortTree(os.path.join(path,x))
            os.chdir(path)
            print('Back in {}'.format(path))

        else: # os.path.isfile(x):

            filePath = os.path.join(path, x)
            destPath = os.path.join(os.path.split(path)[0], x)
            print('Moving: {} to {}'.format(filePath, destPath))
            os.rename(filePath, destPath)




testPath = r"C:\Users\jaker\Desktop\fileOrgTesting - Copy"

unsortTree(testPath)