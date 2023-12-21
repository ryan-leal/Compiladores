import sys
import re

digits = set("0123456789")
minLetters = set("abcdefghijklmnopqrstuvwxyz")
identifierLetters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789")
delimiters = set(":.,;()")
spaces = set(" \t\n")

def build_regex():
    # All pascal regex in groups
    patternsPascal = [
#        ('COMMENT', r'{[\S\s]*?}'),
#        ('OPENNED_COMMENT', r'{[\S\s]*[^}]'),
        ('RESERVED_WORD', r'\b(program|var|integer|real|boolean|procedure|begin|end|if|then|else|while|do|not)\b'),
        ('REAL', r'\b\d+\.\d*'),
        ('INTEGER', r'\b\d+\b'),
#        ('ASSIGNMENT', r':='),
#        ('RELATIONAL_OPERATOR', r'(<=|>=|<>|>|<|=)'),
#        ('ADDITIVE_OPERATOR', r'(\+|-|\bor\b)'),
#        ('MULTIPLICATION_OPERATOR', r'(\*|/|\band\b)'),
        ('IDENTIFIER', r'\b[a-z][a-zA-Z0-9_]*\b'),
        ('DELIMITER', r'[;\.:\(\),]'),
#        ('ERROR_INVALID_TOKEN',r'[^A-Za-z0-9=<>:;_\+\-\*\/{}\t\s.]')
    ]

    # Combine all regex groups using OR operator, compile and return the regex
    combined_pattern = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in patternsPascal)
    regex = re.compile(combined_pattern)
    return regex

# Classe que irá conter o automato
class FiniteAutomaton:
    #Construtor contendo...
    def __init__(self):
        self.states = {'q1', 'q2','q3','q4','q5','q6'} # Estados do automato
        self.current_state = 'q1' # Estado atual, inicialmente é o inicial
        self.accept_state = {'q3','q4','q5','q6'} # Estados de aceitacao
        self.regex = build_regex()
        self.buffer = ""
        self.lineCount = 1

    # Funcao com as transicoes possiveis, recebe o input do automato
    def transition(self, char):
        # Q1 TRANSITIONS
        if self.current_state == 'q1' and char in spaces:
            print("Q1 -> Q1 : Spaces")
        elif self.current_state == 'q1' and re.match(r'[a-z]', char):
            print(f'Q1 -> Q3 : {char}')
            self.buffer += char
            self.current_state = 'q3'
        elif self.current_state == 'q1' and re.match(r'\d', char):#q1->inteiro->q4
            print(f'Q1 -> Q4: line {self.lineCount} - {char}')
            self.current_state = 'q4'
            self.buffer += char
        elif self.current_state == 'q1' and re.match(r'[;\.:\(\),]', char):
            print(f'Q1 -> Q6: line {self.lineCount} - {char}')
            self.current_state = 'q6'
            self.buffer += char
        # Q2 TRANSITION
        elif self.current_state == 'q2' and char != '}':
            return
        # Q3 TRANSITIONS
        elif self.current_state == 'q3' and re.match(r'[a-zA-Z0-9]', char):
            print(f'Q3 -> Q3 : {char}')
            self.buffer += char
        #Q4 TRANSITIONS
        elif self.current_state == 'q4' and re.match(r'\d', char):#q4->inteiro->q4
            print(f'Q4 -> Q4: {char}')
            self.buffer += char
        elif self.current_state == 'q4' and char =='.':#q4->.->q5
            print('Q4 -> Q5: Integer to Real')
            self.buffer += char
            self.current_state = 'q5'
    #Q5 TRANSITIONS
        elif self.current_state == 'q5' and re.match(r'\d', char):#q5->real->q5
            print(f'Q5 -> Q5: Real - {char}')
            self.buffer += char
            self.current_state = 'q5'             
        else:
            for match in self.regex.finditer(self.buffer):
                print(f'{self.current_state.upper()} -> Q1: Line {self.lineCount} - {match.lastgroup}: {match.group()} ')
            # Caso nao haja nenhuma transicao disponivel
            print(f'{self.current_state.upper()} -> Q1 : Sem transicao')
            self.current_state = 'q1'
            self.buffer = ""
        
                
    # Verifica se o automato esta em um estado de aceitacao
    def is_accepted(self):
        return self.current_state in self.accept_state

    # Recebe a string e faz as transicoes para cada caractere
    #  e por ultimo verifica se o ultimo estado é de aceitacao
    def process_input(self, input_string):
        for char in input_string:
            if char == '\n':
                self.lineCount += 1
            self.transition(char)
        return self.is_accepted()


# Open and close input file
def getProgramFile(fileInput):
    with open(fileInput, 'r') as opennedFile:
        data = opennedFile.read()
    return data

# Define uma função main que é chamada no começo do programa
def main():
    args = sys.argv
    input_string = getProgramFile(args[1])

    automaton = FiniteAutomaton() # Construtor do automato

    automaton.process_input(input_string)

# Executado no começo do programa
if __name__ == "__main__":
    main() # Chama a funcao com os comando da main
    