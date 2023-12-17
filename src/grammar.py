import re
import sys # Used to argv

def match(input):
    pascalGrammar = {
        "program" : "palavra reservada",
        "var" : "palavra reservada",
        "integer" : "palavra reservada",
        "real" : "palavra reservada",
        "boolean" : "palavra reservada",
        "procedure" : "palavra reservada",
        "begin" : "palavra reservada",
        "end" : "palavra reservada",
        "if" : "palavra reservada",
        "then" : "palavra reservada",
        "else" : "palavra reservada",
        "while" : "palavra reservada",
        "do" : "palavra reservada",
        "not" : "palavra reservada",
        ";" : "delimitador"
    }
    if pascalGrammar[input]:
        print(input + ' eh ' + pascalGrammar[input])

def getProgramFile(fileInput):
    patternsPascal = [
        ('PALAVRA_RESERVADA', r'\b(program|var|integer|real|boolean|procedure|begin|end|if|then|else|while|do|not)\b'),
        ('ATRIBUICAO', r':='),
        ('RELACIONAIS', r'(<=|>=|<>|>|<|=)'),
        ('OPERADORES_ADITIVOS', r'(\+|-|\bor\b)'),
        ('OPERADORES_MULTIPLICATIVOS', r'(\*|/|\band\b)'),
        ('DELIMITADOR', r'[;.:\(\),]')
    ]
    opennedFile = open(fileInput, 'r')
    data = opennedFile.read()
    print(data)
    line = 1
    index = 1

    combined_pattern = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in patternsPascal)
    regex = re.compile(combined_pattern)

    for match in regex.finditer(data):
        start, end = match.span()
        index = end - data.rfind('\n', 0, start)
        # Atualize a linha atual
        line += data.count('\n', start, end)
        print(data.count('\n', start, end))
        print(str(line) + ' ' + match.group() + ' ' + match.lastgroup)

        

    
      

def main():
    args = sys.argv
    # Printing how arguments works
    #for arguments in args:
    #    print(arguments)
    getProgramFile(args[1])

if __name__ == "__main__":
    main()