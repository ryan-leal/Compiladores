# import re -> Will be used to grammar
import sys # Used to argv

def match(input):
    palavrasReservadas = "program", "var", "integer", "then", "begin", "end", "real"
    for palavras in palavrasReservadas:
        if palavras in input:
            print(input + ' eh ' + palavras)

def getProgramFile(fileInput):
    opennedFile = open(fileInput, 'r')
    data = opennedFile.readlines()
    print(data)
    for linhas in range(len(data)):
        match(data[linhas])
    
      

def main():
    args = sys.argv
    # Printing how arguments works
    #for arguments in args:
    #    print(arguments)
    getProgramFile(args[1])

if __name__ == "__main__":
    main()