import sys # Used to argv
import lexic
import syntactic


def main():
    args = sys.argv
    tokenList = lexic.lexer(args[1]) # call the lexical analyzer with path to pascal file
    syntactic.synAnalysis(tokenList) # call syntactic w/ tokens as arguments

#    if re.search(r'[\s\S]+(\.pas)', args[1]) :
#       Only pascal files...        
#    else:
#        print('Only .pas files allowed')

if __name__ == "__main__":
    main()