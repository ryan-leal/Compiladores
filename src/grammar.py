# import re -> Will be used to grammar
import sys # Used to argv

def getProgramFile(fileInput):
    opennedFile = open(fileInput, 'r')
    data = opennedFile.read()
    print(data)
      

def main():
    args = sys.argv
    # Printing how arguments works
    #for arguments in args:
    #    print(arguments)
    getProgramFile(args[1])

if __name__ == "__main__":
    main()