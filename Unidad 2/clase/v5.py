"Desarrollado por JOSE ANDRIK MARTINEZ RODRIGUEZ"
# Definimos la tabla de transiciones como un diccionario de diccionarios
transition_table = {
    0: {'a': 5, '*': 5, '/': 1},
    1: {'a': 5, '*': 2, '/': 5},
    2: {'a': 2, '*': 3, '/': 2},
    3: {'a': 2, '*': 3, '/': 4},
    4: {'a': 5, '*': 5, '/': 5},
    5: {'a': 5, '*': 5, '/': 5},
}

accept_states = {4: True}
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
        state = transition_table[state][symbol]
    return accept_states.get(state, False)


# Ejemplo de uso
input_string = "/*a*/"
print(simulate_dfa(input_string))  # Devuelve True
input_string = "/**/"
print(simulate_dfa(input_string))  # Devuelve True
input_string = "/***/"
print(simulate_dfa(input_string))  # Devuelve True
input_string = "/*aaa*aaa*/"
print(simulate_dfa(input_string))  # Devuelve True
input_string = "/*a/a*/"
print(simulate_dfa(input_string))  # Devuelve True


# Ejemplo de uso
input_string = "/**"
print(simulate_dfa(input_string))  # Devuelve False
input_string = "/**/a/*aa/"
print(simulate_dfa(input_string))  # Devuelve False
input_string = "aaa/**/aa"
print(simulate_dfa(input_string))  # Devuelve False
input_string = "/*/"
print(simulate_dfa(input_string))  # Devuelve False
input_string = "/**a/"
print(simulate_dfa(input_string))  # Devuelve False
input_string = "//aaaa"
print(simulate_dfa(input_string))  # Devuelve False
