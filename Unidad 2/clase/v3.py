# # Definimos la tabla de transiciones como un diccionario de diccionarios
# transition_table = {
#     0: {'/': 1, '*': 0, 'other': 0},
#     1: {'/': 1, '*': 2, 'other': 0},
#     2: {'/': 2, '*': 3, 'other': 2},
#     3: {'/': 2, '*': 3, 'other': 2},
# }

# # Definimos la lista de estados finales como un diccionario
# accept_states = {2: True}

# # Definimos la función de simulación del DFA


# def simulate_dfa(input_string):
#     state = 0
#     for char in input_string:
#         if char == '/':
#             symbol = '/'
#         elif char == '*':
#             symbol = '*'
#         else:
#             symbol = 'other'
#         state = transition_table[state][symbol]
#     return accept_states.get(state, False)


# # Ejemplo de uso
# input_string = "/*a*/"
# print(simulate_dfa(input_string))  # Devuelve True

# input_string = "/**"
# print(simulate_dfa(input_string))  # Devuelve False
