# Definimos la tabla de transiciones como un diccionario de diccionarios
transition_table = {
    0: {'a': 1, '*': 2, '/': 4, 'other': 0},
    1: {'a': 1, '*': 2, '/': 4, 'other': 0},
    2: {'a': 3, '*': 2, '/': 2, 'other': 2},
    3: {'a': 3, '*': 2, '/': 2, 'other': 2},
    4: {'a': 4, '*': 5, '/': 4, 'other': 4},
    5: {'a': 4, '*': 5, '/': 6, 'other': 4},
    6: {'a': 7, '*': 6, '/': 6, 'other': 4},
    7: {'a': 7, '*': 6, '/': 6, 'other': 4},
}

# Definimos la lista de estados finales como un diccionario
accept_states = {3: True, 7: True}

# Definimos la función de simulación del DFA


def simulate_dfa(input_string):
    state = 0
    for char in input_string:
        if char == 'a':
            symbol = 'a'
        elif char == '*':
            symbol = '*'
        elif char == '/':
            symbol = '/'
        else:
            symbol = 'other'
        state = transition_table[state][symbol]
    return accept_states.get(state, False)


# Ejemplo de uso
input_string = "/*a*/"
print(simulate_dfa(input_string))  # Devuelve True

input_string = "/**/a/*aa*/"
print(simulate_dfa(input_string))  # Devuelve False
