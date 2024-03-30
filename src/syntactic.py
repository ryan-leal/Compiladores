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

########## SEMANTIC FUNCTIONS ################
    
def findInStack(var):
    global symbolStack
    if var == symbolStack[1][0]:
        print('ERROR: TRYING TO USE PROGAM NAME ' + var)
        sys.exit()
    for values in symbolStack:
        if values[0] == var:
            print(var + ' found in stack, can be used')
            return values[1]
    print('ERROR: TRYING TO USE UNDECLEARED VAR NAMED ' + var)
    sys.exit()

def cleanStack():
    global symbolStack
    print('=====Before Clean Stack Scope=========')
    print(symbolStack)
    while symbolStack[-1] != ('mark', None):
        symbolStack.pop()
    symbolStack.pop()
    print('=====After Clean Stack Scope=========')
    print(symbolStack)

def isInStack(var):
    global identifierStack, symbolStack
    if var == symbolStack[1][0]:
        print('ERROR: TRYING TO DECLARE ' + var + ' BUT IT\'S THE PROGRAM NAME')
        sys.exit()
    for x in symbolStack[::-1]:
        if x == ('mark', None):
            print(var + ' NOT FOUNDED IN SCOPE, CAN BE DECLARED')
            break
        if var in x:
            print('ERROR: TRYING TO DECLARE ' + var + ' BUT IS ALREADY DECLARED IN SCOPE')
            sys.exit()

def stackAppend(typeStack):
    global identifierStack, symbolStack
    for vars in identifierStack:
        isInStack(vars)
        symbolStack.append((vars, typeStack))
    identifierStack = []

def updateTypeStack(resultType):
    global typeControlStack
    typeControlStack.pop()
    typeControlStack.pop()
    typeControlStack.append(resultType)

def typeStackChecker(isRel = 0, isBoolOp = 0):
    global typeControlStack
    if isBoolOp:
        if typeControlStack[-1] == 'boolean' and typeControlStack[-2] == 'boolean':
            print('Boolean Operation beetween two booleans - OK')
            updateTypeStack('boolean')
            print(typeControlStack)
        else:
            print('ERROR: TRYING TO MAKE A BOOLEAN OPERATION BETWEEN ' + typeControlStack[-1] +' AND ' + typeControlStack[-2])
            sys.exit()
    else:
        if typeControlStack[-1] == 'integer' and typeControlStack[-2] == 'integer':
            print('Operation between integer and integer - OK')
            if isRel:
                updateTypeStack('boolean')
                print('Relational Operation - boolean output')
            else:
                updateTypeStack('integer')
        elif (typeControlStack[-1] == 'integer' and typeControlStack[-2] == 'real') or (typeControlStack[-1] == 'real' and typeControlStack[-2] == 'integer'):
            print('Operation between integer and real - OK')
            if isRel:
                updateTypeStack('boolean')
                print('Relational Operation - boolean output')
            else:
                updateTypeStack('real')
        elif typeControlStack[-1] == 'real' and typeControlStack[-2] == 'real':
            print('Operation between real and real - OK')
            if isRel:
                updateTypeStack('boolean')
                print('Relational Operation - boolean output')
            else:
                updateTypeStack('real')
        else:
            print('ERROR: TRYING TO MAKE A OPERATION BETWEEN ' + typeControlStack[-1] +' AND ' + typeControlStack[-2])
            sys.exit()
    
def assignStackChecker():
    global typeControlStack
    if typeControlStack[-1] == 'integer' and typeControlStack[-2] == 'integer':
        print('Assignment between integer and integer - OK')
        typeControlStack = []
        print(typeControlStack)
    elif typeControlStack[-1] == 'integer' and typeControlStack[-2] == 'real':
        print('Assignment between integer and real - OK')
        typeControlStack = []
        print(typeControlStack)
    elif typeControlStack[-1] == 'real' and typeControlStack[-2] == 'real':
        print('Assignment between real and real - OK')
        typeControlStack = []
        print(typeControlStack)
    elif typeControlStack[-1] == 'boolean' and typeControlStack[-2] == 'boolean':
        print('Assignment between boolean and boolean - OK')
        typeControlStack = []
        print(typeControlStack)
    else:
        print('ERROR: TRYING TO ASSIGN A ' + typeControlStack[-1] +' IN A ' + typeControlStack[-2] + ' VAR')
        sys.exit()

def verifyBooleanResult():
    global typeControlStack
    print('Verifying if a Boolean value is resulted after IF / WHILE Expression Analysis...')
    if typeControlStack[-1] == 'boolean':
        print('Boolean Value at the top of typeControlStack - OK')
        print(typeControlStack)
        typeControlStack.pop()
        print('Stack Top Cleaned...')
        print(typeControlStack)
    else:
        print(typeControlStack)
        print('ERROR: AFTER IF / WHILE STATEMENT, TOP MUST BE AN BOOLEAN')
        sys.exit()

def clearTopTypeStack():
    global typeControlStack
    typeControlStack.pop()
    print('Cleaning top of TypeControlStack...')
    print(typeControlStack)

###################################################

def listIdentifier(isArgs = 0):
    global analyzer, token, symbolStack, identifierStack
    if isArgs == 1 and token[0] == ')':
        return 
    if token[1] == 'IDENTIFIER':
        print('Identifier found in args/var: ' + token[0])
        # Adding identifier to a stack of identifiers, after will be used to add in SymbolStack
        identifierStack.append(token[0])
        print(identifierStack)
        token = analyzer.next()
        print('Next token: ' + token[0])
        if token[0] == ',':
            print('Found \',\' in declaration, identifier expected next')
            token = analyzer.next()
            if isArgs == 1:
                listIdentifier(isArgs=1)
            else:
                listIdentifier()
            return                      
        if token[0] == ':':
            token = analyzer.next()
            if token[0] == 'integer' or token[0] == 'real' or token[0] == 'boolean':
                print('Data Type found: ' + token[0])
                typeStack = token[0]
                token = analyzer.next()
                print('Next token should be \';\' or \')\': ' + token[0])
                if token[0] == ';':
                    token = analyzer.next()
                    stackAppend(typeStack)
                    print('VAR DECLARED, next token: ' + token[0])
                    return
                else:
                    if isArgs == 1 and token[0] == ')':
                        print('Its the last argument, dont need ;')
                        stackAppend(typeStack)
                        return
                    elif isArgs == 1:
                        print('ERROR: EXPECTED \')\' OR \';\' BUT ' + token[0] + ' FOUND IN LINE ' + token[2])
                        sys.exit()
                    else:
                        print('ERROR: EXPECTED \';\' BUT FOUND ' + token[0] +' IN LINE ' + token[2])
                        sys.exit()
            else:
                print('ERROR: DATA TYPE EXPECTED BUT FOUND' + token[0] + 'IN LINE ' + token[2])
                sys.exit()
        else:
            print('ERROR: EXPECTED \':\' BUT FOUND' + token[0] + 'IN LINE ' + token[2])
            sys.exit()
    else:
        print('ERROR: IDENTIFIER EXPECTED BUT FOUND' + token[0] + 'IN LINE ' + token[2])
        sys.exit()

def varDeclaration():
    global analyzer, token 
    if token[0] == 'var':
        print('\'var\' found, declaration analysis...')
        token = analyzer.next()
        # If after found var, there anything inside... return error
        if not(token[1] == 'IDENTIFIER'):
            print('ERROR: IDENTIFIER EXPECTED BUT \'' + token[0] + '\' FOUND IN LINE '+ token[2])
            sys.exit() # Stop program
        while token[0] != 'begin' and token[0] != 'procedure':
            listIdentifier()
    else:
        print('\'var\' not found, but ' + token[0])

def subProgramDeclarations():
    global analyzer, token
    while(token[0] != 'begin'):
        subProgramDeclaration()

def subProgramDeclaration():
    global analyzer, token, symbolStack
    if token[0] == 'procedure':
            print('I found \'procedure\'')
            token = analyzer.next()
            symbolStack.append((token[0], 'procedure'))
            symbolStack.append(('mark', None))
            if token[1] == 'IDENTIFIER':
                token = analyzer.next()
                if token[0] == '(':
                    token = analyzer.next()
                    while token[0] != ')':
                        listIdentifier(1)
                    if token[0] == ')':
                        token = analyzer.next()
                        if token[0] == ';':
                            token = analyzer.next()
                            varDeclaration()
                            subProgramDeclarations()
                            compoundCommand()
                            cleanStack()
                            return
                        else:
                            if token[0] == 'end':
                                print('Dont found ; but found end...')
                                return
                            print('ERROR: EXPECTED \';\' BUT ' + token[0] + ' FOUND IN LINE ' + token[2])
                            sys.exit()
                    else:
                        print('ERROR: EXPECTED \')\' BUT ' + token[0] + ' FOUND IN LINE ' + token[2])
                        sys.exit()                      
                elif token[0] == ';':
                    print('No parenthesis found, but \';\'')
                    token = analyzer.next()
                    varDeclaration()
                    subProgramDeclaration()
                    compoundCommand()
                    cleanStack()
                    return
                else:
                    print('ERROR: EXPECTED \'(\' OR \';\' BUT ' + token[0] + ' FOUND IN LINE ' + token[2])
                    sys.exit()
            else:
                print('ERROR: EXPECTED IDENTIFIER BUT ' + token[1] + ' IN LINE ' + token[2])
                sys.exit()
    else:
        print('procedure dont found but ' + token[0])

def isFactor():
    global token, analyzer, typeControlStack
    if token[1] == 'IDENTIFIER':
        print('Identifier Factor found: ' + token[0])
        typeControlStack.append(findInStack(token[0]))
        print(typeControlStack)
        token = analyzer.next()
        if token[0] == '(':
            token = analyzer.next()
            print('Identifier Factor - Parenthesis START -')
            expressionList()
            token = analyzer.next()
            if token[0] == ')':
                token = analyzer.next()
                print('Identifier Factor - Parenthesis FINISH -')
                typeControlStack.pop()
                return True
            else:
                print('ERROR: EXPECTED \')\' BUT FOUND ' + token[0] + ' IN LINE ' + token[2])
                sys.exit()
        return True
    elif token[1] == 'INTEGER':
        print('Integer Factor found: ' + token[0])
        typeControlStack.append('integer')
        print(typeControlStack)
        token = analyzer.next()
        return True
    elif token[1] == 'REAL':
        print('Real Factor Found: ' + token[0])
        typeControlStack.append('real')
        print(typeControlStack)
        token = analyzer.next()
        return True
    elif token[1] == 'BOOLEAN':
        print('Boolean Factor Found: ' + token[0])
        typeControlStack.append('boolean')
        print(typeControlStack)
        token = analyzer.next()
        return True
    elif token[0] == 'not':
        print('\'not\' factor found: ' + token[0])
        token = analyzer.next()
        if isFactor():
            return True
        else:
            print('ERROR: EXPECTED \'A FACTOR IN NOT\' BUT FOUND ' + token[0] + ' IN LINE ' + token[2])
            sys.exit()  
    elif token[0] == '(':
        print('Parenthesis Factor found: ' + token[0])
        token = analyzer.next()
        expressionAnalyzer()
        if token[0] == ')':
            token = analyzer.next()
            print('Expression inside parenthesis factor - Finished -')
            return True
        else:
            print('ERROR: EXPECTED \')\' BUT FOUND ' + token[0] + ' IN LINE ' + token[2])
            sys.exit()

def isTerm():
    global token, analyzer
    isFactor()
    if token[1] == 'MULTIPLICATION_OPERATOR':
        print('Multiplication Operator Found in TermChecker: ' + token[0])
        if token[0] == 'and':
            isBoolOp = 1
        else:
            isBoolOp = 0
        token = analyzer.next()
        isTerm()
        typeStackChecker(isBoolOp=isBoolOp)
    return True       

def expressionSimple():
    global token, analyzer
    if token[0] == '+' or token[0] == '-':
        token = analyzer.next()
    isTerm()
    if token[1] == 'ADDITIVE_OPERATOR':
        print('Additive Operator found in SimpleExp: ' + token[0])
        if token[0] == 'or':
            isBoolOp = 1
        else:
            isBoolOp = 0
        token = analyzer.next()
        expressionSimple()
        typeStackChecker(isBoolOp=isBoolOp)

def expressionAnalyzer():
    global token, analyzer
    expressionSimple()
    if token[1] == 'RELATIONAL_OPERATOR':
        print('Relational Operator found in expAnalyzer: ' + token[0])
        token = analyzer.next()
        expressionSimple()
        typeStackChecker(isRel=1)

def expressionList():
    global token, analyzer
    expressionAnalyzer()
    if token[0] == ',':
        print('Comma found in exp list: ' + token[0])
        token = analyzer.next()
        expressionList()

def commands():
    global token, analyzer, typeControlStack
    print('Inside Commands with token: ' + token[0])
    if token[1] == 'IDENTIFIER':
        print('identifier Found, token: ' + token[0])
        typeControlStack.append(findInStack(token[0]))
        print(typeControlStack)
        token = analyzer.next()
        if token[0] == ':=':
            print('I found :=, so its a attribuition')
            token = analyzer.next()
            expressionAnalyzer()
            print(typeControlStack)
            assignStackChecker()
            print('Attribution found in line ' + token[2])
            return
        elif token[0] == '(':
            print('its a procedure call using ()')
            clearTopTypeStack()
            token = analyzer.next()
            expressionList()
            if token[0] == ')':
                token = analyzer.next()
                if token[0] == ';':
                    print('Procedure call found in line ' + token[2])
                    clearTopTypeStack()
                    token = analyzer.next()
                    return
                else:
                    print('ERROR: EXPECTED \';\' BUT ' + token[0] + ' FOUND IN LINE ' + token[2])
                    sys.exit()
            else:
                print('ERROR: EXPECTED \')\' BUT ' + token[0] + ' FOUND IN LINE ' + token[2])
                sys.exit()
        elif token[0] == ';':
            print('its a procedure call using \';\' in line ' + token[2])
            clearTopTypeStack()
            token = analyzer.next()
            return
        else:
            print('ERROR: EXPECTED \':=\' OR \';\' OR \'();\' BUT ' + token[0] + ' FOUND IN LINE ' + token[2])
            sys.exit()
    else:
        if token[1] == 'RESERVED_WORD':
            print('Reserved Word Found, token: ' + token[0])
            if token[0] == 'begin':
                print('\'begin\' found inside \'begin\'')
                compoundCommand()
            elif token[0] == 'if':
                print('Found \'if\' command')
                token = analyzer.next()
                expressionAnalyzer()
                if token[0] == 'then':
                    verifyBooleanResult()
                    print('Found \'Then\' command')
                    token = analyzer.next()
                    commands()
                    if token[0] == 'else':
                        print('Found \'Else\' Statement')
                        token = analyzer.next()
                        commandList()
                        return
                    else:
                        print('No \'else\' statement found')
                        return
                else:
                    print('ERROR: EXPECTED \'then\' BUT ' + token[0] + ' FOUND IN LINE ' + token[2])
                    sys.exit()
            elif token[0] == 'while':
                print('Found \'while\' command')
                token = analyzer.next()
                expressionAnalyzer()
                if token[0] == 'do':
                    verifyBooleanResult()
                    print('\'Do\' command found')
                    token = analyzer.next()
                    commandList()
                    return
                else:
                    print('ERROR: EXPECTED \'do\' BUT ' + token[0] + ' FOUND IN LINE ' + token[2])
                    sys.exit()  
        else:
            print('ERROR: NO COMMAND FOUND: ' + token[0] + ' IN LINE ' + token[2])
            sys.exit()

def commandList():
    global token, analyzer
    commands()
    if token[0] == ';':
        token = analyzer.next()
        commandList()

def compoundCommand():
    global token, analyzer
    if token[0] == 'begin':
        print('Found \'begin\'')
        token = analyzer.next()
        while token[0] != 'end':
            commandList()
        print('FINISHED COMMAND LIST WITH TOKEN: ' + token[0] + ' IN LINE ' + token[2])
        if token[0] == 'end':
            print('I found a \'end\' after begin')
            token = analyzer.next()
            if token[0] == ';':
                token = analyzer.next()
        else:
            print('ERROR: EXPECTED \'end\' BUT ' + token[0] + ' IN LINE ' + token[2])
            sys.exit()

    else:
        print('ERROR: EXPECTED \'begin\' BUT ' + token[0] + ' IN LINE ' + token[2])
        sys.exit()

def synAnalysis(tokenList):
    global symbolStack, identifierStack, typeControlStack
    symbolStack = [('mark', None)]
    identifierStack = []
    typeControlStack = []
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
            symbolStack.append((token[0], 'program'))
            token = analyzer.next()
            if token[0] == ';':
                token = analyzer.next()
                varDeclaration()
                subProgramDeclarations()
                compoundCommand()
                cleanStack()
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
    