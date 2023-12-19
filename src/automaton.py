# Classe que irá conter o automato
class FiniteAutomaton:
    #Construtor contendo...
    def __init__(self):
        self.states = {'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13'} # Estados do automato
        self.current_state = 'q1' # Estado atual, inicialmente é o inicial
        self.accept_state = {'q3','q4','q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13'} # Estados de aceitacao

    # Funcao com as transicoes possiveis, recebe o input do automato
    def transition(self, char):
        if self.current_state == 'q1' and char == ' ':
            self.current_state = 'q1'
        elif self.current_state == 'q1' and char == '{':#comentarios-abre chave
            self.current_state = 'q2'
        elif self.current_state == 'q2' and char == 'regex':#comentarios-V menos}
            self.current_state = 'q2'
        elif self.current_state == 'q2' and char == '}':#comentarios-fecha chave
            self.current_state = 'q1'
        elif self.current_state == 'q1' and char == 'regex':#identidicador
            self.current_state = 'q3'
        elif self.current_state == 'q3' and char == 'regex':#identidicador iterativo
            self.current_state = 'q3'
        elif self.current_state == 'q1' and char == 'regex':#numero
            self.current_state = 'q4'
        elif self.current_state == 'q4' and char == 'regex':#numero-iterativo
            self.current_state = 'q4'
        elif self.current_state == 'q1' and char == '.':
            self.current_state = 'q5'
        elif self.current_state == 'q1' and char == '+':
            self.current_state = 'q8'
        elif self.current_state == 'q1' and char == ';':
            self.current_state = 'q7'
        elif self.current_state == 'q1' and char == '*':
            self.current_state = 'q10'
        elif self.current_state == 'q1' and char == '(':
            self.current_state = 'q9'
        elif self.current_state == 'q1' and char == ')':
            self.current_state = 'q11'
        elif self.current_state == 'q1' and char == ':':
            self.current_state = 'q12'
        elif self.current_state == 'q1' and char == '=':
            self.current_state = 'q13'
        else:
            # Caso nao haja nenhum estado correspondente
            self.current_state = 'invalid'
    
    # Verifica se o automato esta em um estado de aceitacao
    def is_accepted(self):
        return self.current_state == self.accept_state

    # Recebe a string e faz as transicoes para cada caractere
    #  e por ultimo verifica se o ultimo estado é de aceitacao
    def process_input(self, input_string):
        for char in input_string:
            self.transition(char)

        return self.is_accepted()


# Define uma função main que é chamada no começo do programa
def main():
    automaton = FiniteAutomaton() # Construtor do automato
    input_string = 'AAB' # Palavara entrada do automato

    if automaton.process_input(input_string):
        print(f"The string '{input_string}' is accepted.")
    else:
        print(f"The string '{input_string}' is not accepted.")

# Executado no começo do programa
if __name__ == "__main__":
    main() # Chama a funcao com os comando da main
    