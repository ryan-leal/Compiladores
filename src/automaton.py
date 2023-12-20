import sys
import re

digits = set("0123456789")
letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
spaces = set(" \t\n")

def build_regex():
    # All pascal regex in groups
    patternsPascal = [
#        ('COMMENT', r'{[\S\s]*?}'),
#        ('OPENNED_COMMENT', r'{[\S\s]*[^}]'),
        ('RESERVED_WORD', r'\b(program|var|integer|real|boolean|procedure|begin|end|if|then|else|while|do|not)\b'),
#        ('REAL', r'\b\d+\.\d*'),
#        ('INTEGER', r'\b\d+\b'),
#        ('ASSIGNMENT', r':='),
#        ('RELATIONAL_OPERATOR', r'(<=|>=|<>|>|<|=)'),
#        ('ADDITIVE_OPERATOR', r'(\+|-|\bor\b)'),
#        ('MULTIPLICATION_OPERATOR', r'(\*|/|\band\b)'),
#        ('IDENTIFIER', r'\b[a-z][a-zA-Z0-9_]*\b'),
#        ('DELIMITER', r'[;.:\(\),]'),
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
        self.states = {'q0', 'q1', 'q2'} # Estados do automato
        self.current_state = 'q0' # Estado atual, inicialmente é o inicial
        self.accept_state = {'q1', 'q2'} # Estados de aceitacao
        self.buffer = ""

    # Funcao com as transicoes possiveis, recebe o input do automato
    def transition(self, char):
        if self.current_state == 'q0' and char in spaces:
            print("Transicao teste q0 para ele mesmo")
        elif self.current_state == 'q0' and char in digits:
            print('Transicao teste q0 para digitos')
        else:
            # Caso nao haja nenhum estado correspondente
            
            
    
    # Verifica se o automato esta em um estado de aceitacao
    def is_accepted(self):
        return self.current_state in self.accept_state

    # Recebe a string e faz as transicoes para cada caractere
    #  e por ultimo verifica se o ultimo estado é de aceitacao
    def process_input(self, input_string):
        regex = build_regex()
        for char in input_string:
            self.transition(char)
            # Search for Reserved Words
            match = regex.search(self.buffer)  
            if match:
                print(f'I found an {match.lastgroup} : {match.group()}')
                self.buffer = ""

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

    if automaton.process_input(input_string):
        print(f"The string '{input_string}' is accepted.")
    else:
        print(f"The string '{input_string}' is not accepted.")

# Executado no começo do programa
if __name__ == "__main__":
    main() # Chama a funcao com os comando da main
    