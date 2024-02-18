import sys

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

def varDeclaration(token, analyzer):
    if token[0] == 'var':
        print('Achei o VAR')
        token = analyzer.next()
        if token[0] == 'begin' or token[0] == 'procedure':
            print('ERROR: IDENTIFIER EXPECTED BUT \'' + token[0] + '\' FOUND')
            sys.exit()
        while token[0] != 'begin' and token[0] != 'procedure':
            if token[1] == 'IDENTIFIER':
                token = analyzer.next()
                if token[0] == ',':
                    token = analyzer.next()
                    continue                          
                if token[0] == ':':
                    token = analyzer.next()
                    if token[0] == 'integer' or token[0] == 'real' or token[0] == 'boolean':
                        token = analyzer.next()
                        if token[0] == ';':
                            print('Var Declared')
                            token = analyzer.next()
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
    else:
        print('Não tem VAR, achei o ' + token[0])

def subProgramDeclaration(token, analyzer):
    if token[0] == 'procedure':
            print('I found procedure')
            token = analyzer.next()
            if token[1] == 'IDENTIFIER':
                token = analyzer.next()
                if token[0] == '(':
                    print('open parenthesis')
                    token = analyzer.next()
                    # while token[0] != ')':
                    #     if token[1] == 'IDENTIFIER':
                    #         token = analyzer.next()
                    #         if token[0] == ';':
                    #             token = analyzer.next()
                    #             continue                          
                    #         if token[0] == ':':
                    #             token = analyzer.next()
                    #             if token[0] == 'integer' or token[0] == 'real' or token[0] == 'boolean':
                    #                 token = analyzer.next()
                    #                 if token[0] == ';':
                    #                     print('Var Declared')
                    #                     token = analyzer.next()
                    #                 else:
                    #                     print('ERROR: DELIMITER \';\' EXPECTED IN LINE ' + token[2])
                    #                     sys.exit()
                    #             else:
                    #                 print('ERROR: DATA TYPE EXPECTED IN LINE ' + token[2])
                    #                 sys.exit()
                    #         else:
                    #             print('ERROR: DELIMITER \':\' EXPECTED IN LINE ' + token[2])
                    #             sys.exit()
                    #     else:
                    #         print('ERROR: IDENTIFIER EXPECTED IN LINE ' + token[2])
                    #         sys.exit()
                else:
                    print('ERROR: EXPECTED \'(\' BUT ' + token[0] + ' FOUND')
            else:
                print('ERROR: IDENTIFIER EXPECTED IN LINE ' + token[2])
                sys.exit()
    else:
        print('procedure dont found but ' + token[0])


def compostCommand():
    print('No comando Composto')

def synAnalysis(tokenList):
    analyzer = tokenAnalyzer(tokenList)
    token = analyzer.next()

    if token[0] == 'program':
        token = analyzer.next()
        if token[1] == 'IDENTIFIER':
            token = analyzer.next()
            if token[0] == ';':
                token = analyzer.next()
                varDeclaration(token, analyzer)
                subProgramDeclaration(token, analyzer)
                compostCommand()
            if token[0] != '.':
                print('Erro, programa nao termina em ponto')
            else:
                print('Aceito!')
                
        
