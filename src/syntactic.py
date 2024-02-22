import sys # Used to stop program when error is 

# tokenList class, return next token
class tokenAnalyzer:
    def __init__(self, tokenList):
        self.tokens = tokenList
        self.posicao_atual = 0  # Inicializa a posição atual como 0

    def next(self):
        if self.posicao_atual < len(self.tokens):
            token = self.tokens[self.posicao_atual]
            self.posicao_atual += 1
            return token
        else:
            return None  # Retorna None se não houver mais tokens

def listIdentifier():
    global analyzer, token 
    if token[1] == 'IDENTIFIER':
        print('Token before next in listIdentifier: ' + token[0])
        token = analyzer.next()
        print('Token after next in listIdentifier: ' + token[0])
        if token[0] == ',':
            print('Entered in \',\' if statement')
            token = analyzer.next()
            listIdentifier()
            return                      
        if token[0] == ':':
            token = analyzer.next()
            print('Token after : in listIdentifier: ' + token[0])
            if token[0] == 'integer' or token[0] == 'real' or token[0] == 'boolean':
                token = analyzer.next()
                print('Token after type in listIdentifier: ' + token[0])
                if token[0] == ';':
                    print('Var Declared')
                    token = analyzer.next()
                    print('Var Declared, next token ' + token[0])
                    return token
                else:
                    print('ERROR: DELIMITER \';\' EXPECTED IN LINE ' + token[2])
                    sys.exit()
            else:
                print('ERROR: DATA TYPE EXPECTED IN LINE ' + token[2])
                sys.exit()
        else:
            print('ERROR: DELIMITER \':\' EXPECTED IN LINE ' + token[2])
            sys.exit()
    else:
        print('ERROR: IDENTIFIER EXPECTED IN LINE ' + token[2])
        sys.exit()

def varDeclaration():
    global analyzer, token 
    if token[0] == 'var':
        print('Var found... var declaration analysis')
        token = analyzer.next()
        # If after found var, there anything inside... return error
        if token[0] == 'begin' or token[0] == 'procedure':
            print('ERROR: IDENTIFIER EXPECTED BUT \'' + token[0] + '\' FOUND')
            sys.exit() # Stop program
        while token[0] != 'begin' and token[0] != 'procedure':
            listIdentifier()
            print('Token after return to varDeclaration: ' + token[0])
    else:
        print('Não tem VAR, achei o ' + token[0])

def subProgramDeclaration():
    global analyzer, token 
    if token[0] == 'procedure':
            print('I found procedure')
            token = analyzer.next()
            if token[1] == 'IDENTIFIER':
                token = analyzer.next()
                if token[0] == '(':
                    print('open parenthesis')
                    token = analyzer.next()                      
                elif token[0] == ';':
                    print('Nao tinha parentesis mas tinha ponto e virgula')
                    token = analyzer.next()
                else:
                    print('ERROR: EXPECTED \'(\' OR \';\' BUT ' + token[0] + ' FOUND')
                    sys.exit()
            else:
                print('ERROR: EXPECTED IDENTIFIER BUT ' + token[1] + ' IN LINE ' + token[2])
                sys.exit()
    else:
        print('procedure dont found but ' + token[0])


def compostCommand():
    if token[0] == 'begin':
        print('I found begin')
    elif token[0] == 'end':
        print('I found end')
    else:
        print('Comandos especiais')
        optionalCommand()
        sys.exit()

def optionalCommand():
    print('Eu sou um comando opcional')

def synAnalysis(tokenList):
    # Instance of tokenAnalyzer to return next token using token list from lexer
    global analyzer, token 
    analyzer = tokenAnalyzer(tokenList)
    token = analyzer.next() # get next token
    # token[0] -> character
    # token[1] -> token identifier
    # token[2] -> Line in file

    if token[0] == 'program':
        token = analyzer.next()
        if token[1] == 'IDENTIFIER':
            token = analyzer.next()
            if token[0] == ';':
                token = analyzer.next()
                varDeclaration()
                subProgramDeclaration()
                compostCommand()
            else:
                print('ERROR: EXPECTED \';\' BUT ' + token[0] + ' FOUND IN LINE ' + token[2])
            if token[0] != '.':
                print('ERROR: EXPECTED \'.\' BUT ' + token[0] + ' FOUND IN LINE ' + token[2])
            else:
                print('PASCAL PROGRAM ACCEPTED')
        else:
            print('ERROR: EXPECTED IDENTIFIER BUT ' + token[1] + ' FOUND IN LINE ' + token[2])
    else:
        print('ERROR: EXPECTED \'program\' BUT ' + token[0] + ' FOUND IN LINE ' + token[2])            
        
