# Classe que irá conter o automato
class FiniteAutomaton:
    #Construtor contendo...
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'} # Estados do automato
        self.current_state = 'q0' # Estado atual, inicialmente é o inicial
        self.accept_state = 'q2' # Estados de aceitacao

    # Funcao com as transicoes possiveis, recebe o input do automato
    def transition(self, char):
        if self.current_state == 'q0' and char == 'A':
            self.current_state = 'q1'
        elif self.current_state == 'q1' and char == 'B':
            self.current_state = 'q2'
        elif self.current_state == 'q1' and char == 'A':
            self.current_state = 'q1'
        elif self.current_state == 'q2' and char == 'B':
            self.current_state = 'q2'
        elif self.current_state == 'q2' and char == 'A':
            self.current_state = 'q1'
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
    