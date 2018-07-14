import os

def unsortTree(path):
    os.chdir(path)

    for x in os.listdir():
        if os.path.isdir(x):
            #unsortTree(os.path.join(path, x))
    for x in os.listdir():
        if os.path.isfile(x):
            filePath = os.path.join(path, x)
            destPath = os.path.join(os.path.split(path)[0], x)
            os.rename(filePath, destPath)