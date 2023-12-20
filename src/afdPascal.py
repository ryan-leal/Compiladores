# Alfabeto
digits = set("0123456789")
letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
whitespace = set(" \t\n")

# Estados
q0 = 'q0'
q1 = 'q1'
q2 = 'q2'

# Estados de Aceitação
accept_states = {q1, q2}

# Transições
transitions = {
    q0: {digit: q1 for digit in digits},
    q0: {letter: q2 for letter in letters},
    q1: {digit: q1 for digit in digits},
    q2: {letter: q2 for letter in letters},
}

print(transitions)

def lexer(input_string):
    current_state = q0
    token = ""

    for char in input_string:
        if char in whitespace:
            print("============================")
            print(f'Char: {char}')
            print(f'New State: {current_state}')
            print(f'Token: {token}')
            print("============================")
            if current_state in accept_states:
                yield token, current_state
            token = ""
            current_state = q0
        elif char in transitions[current_state[char]]:
            print("============================")
            print(f'Char: {char}')
            token += char
            print(f'Token: {token}')
            current_state = transitions[current_state[char]]
            print(f'New State: {current_state}')
            print("============================")
        else:
            print("============================")
            print(f'Char: {char}')
            print(f'New State: {current_state}')
            print(f'Token: {token}')
            print("============================")
            if current_state in accept_states:
                yield token, current_state
            token = char
            current_state = q0

    if current_state in accept_states:
        yield token, current_state

# Exemplo de uso
input_string = "123 if 456 else 789"
for token, state in lexer(input_string):
    print(f"Token: {token}, Estado: {state}")
