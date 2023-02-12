import sys

def main():
    command = sys.argv[1]
    inputpath = sys.argv[2]

    if command == "reverse":
        outputpath = sys.argv[3]
        reverse(inputpath, outputpath)
    
    elif command == "copy":
        outputpath = sys.argv[3]
        copy(inputpath, outputpath)

    elif command == "duplicate-contents":
        n = int(sys.argv[3])
        duplicateContents(inputpath, n)

    elif command == "replace-string":
        needle = sys.argv[3]
        newString = sys.argv[4]
        replaceString(inputpath, needle, newString)
    
    else:
        print("Please enter the corrent command.")
        sys.exit(1)

def readContents(pathname):
    with open(pathname) as f:
        return f.read()

def writeContents(pathname, contents):
    with open(pathname, 'w') as f:
        f.write(contents)

def reverse(inputpath, outputpath):
    contents = readContents(inputpath)
    writeContents(outputpath, contents[::-1])

def copy(inputpath, outputpath):
    contents = readContents(inputpath)
    writeContents(outputpath, contents)

def duplicateContents(inputpath, n):
    contents = readContents(inputpath)
    newContents = n * contents
    writeContents(inputpath, newContents)

def replaceString(inputpath, needle, newString):
    contents = readContents(inputpath)
    newContents = contents.replace(needle, newString)
    writeContents(inputpath, newContents)

if __name__ == '__main__':
    main()