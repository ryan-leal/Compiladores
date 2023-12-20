import sys

digits = set("0123456789")
letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
spaces = set(" \t\n")
reserved_word = ["program", "if", "else", "var"]




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
            print(f"i'm in {self.current_state} and i saw a space")
            self.current_state = 'q0'
            print(f"Now i'm in {self.current_state}")
            if self.buffer in reserved_word:
                print(f"Reserved Word: {self.buffer} found, erasing buffer")
            self.buffer = ""
        elif self.current_state == 'q0' and char in digits:#comentarios-abre chave
            print(f"i'm in {self.current_state} and i saw {char} digit")
            self.current_state = 'q1'
            print(f"Now i'm in {self.current_state}")
        elif self.current_state == 'q0' and char in letters:#comentarios-abre chave
            print(f"i'm in {self.current_state} and i saw {char} letter")
            self.current_state = 'q2'
            print(f"Now i'm in {self.current_state}")
            self.buffer += char
            print(f"Current Buffer: {self.buffer}")
        elif self.current_state == 'q1' and char in spaces:#comentarios-abre chave
            print(f"i'm in {self.current_state} and i saw a space")
            self.current_state = 'q1'
            print(f"Now i'm in {self.current_state}")
            if self.buffer in reserved_word:
                print(f"Reserved Word: {self.buffer} found, erasing buffer")
            self.buffer = ""
        elif self.current_state == 'q1' and char in digits:#comentarios-abre chave
            print(f"i'm in {self.current_state} and i saw {char} digit")
            self.current_state = 'q1'
            print(f"Now i'm in {self.current_state}")
        elif self.current_state == 'q1' and char in letters:#comentarios-abre chave
            print(f"i'm in {self.current_state} and i saw {char} letter")
            self.current_state = 'q2'
            print(f"Now i'm in {self.current_state}")
            self.buffer+=char
            print(f"Current Buffer: {self.buffer}")
        elif self.current_state == 'q2' and char in spaces:#comentarios-abre chave
            print(f"i'm in {self.current_state} and i saw a space")
            self.current_state = 'q2'
            print(f"Now i'm in {self.current_state}")
            if self.buffer in reserved_word:
                print(f"Reserved Word: {self.buffer} found, erasing buffer")
            self.buffer = ""
        elif self.current_state == 'q2' and char in digits:#comentarios-abre chave
            print(f"i'm in {self.current_state} and i saw {char} digit")
            self.current_state = 'q1'
            print(f"Now i'm in {self.current_state}")
        elif self.current_state == 'q2' and char in letters:#comentarios-abre chave
            print(f"i'm in {self.current_state} and i saw {char} letter")
            self.current_state = 'q2'
            print(f"Now i'm in {self.current_state}")
            self.buffer += char
            print(f"Current Buffer: {self.buffer}")
        else:
            # Caso nao haja nenhum estado correspondente
            print('Not a mapped character')
            
    
    # Verifica se o automato esta em um estado de aceitacao
    def is_accepted(self):
        return self.current_state in self.accept_state

    # Recebe a string e faz as transicoes para cada caractere
    #  e por ultimo verifica se o ultimo estado é de aceitacao
    def process_input(self, input_string):
        for char in input_string:
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

    if automaton.process_input(input_string):
        print(f"The string '{input_string}' is accepted.")
    else:
        print(f"The string '{input_string}' is not accepted.")

# Executado no começo do programa
if __name__ == "__main__":
    main() # Chama a funcao com os comando da main
    