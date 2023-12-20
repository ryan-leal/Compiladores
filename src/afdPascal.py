pascalPatterns=[
    ('digits', "0123456789"),
    ('letters', "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
]
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
    q0: {digits in pascalPatterns: q1, letters in pascalPatterns: q2},
    q1: {digits in pascalPatterns: q1},
    q2: {letters in pascalPatterns: q2},
}

def lexer(input_string):
    current_state = q0
    token = ""

    for char in input_string:
        if char in whitespace:
            if current_state in accept_states:
                yield token, current_state
            token = ""
            current_state = q0
        elif char in transitions[current_state]:
            token += char
            current_state = transitions[current_state][char]
        else:
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
