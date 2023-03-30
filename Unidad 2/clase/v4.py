# # Definimos la tabla de transiciones
# transition_table = [[1, 0, 0], [2, 1, 0], [2, 2, 3], [2, 2, 0]]

# # Definimos la lista de estados finales
# accept_states = [False, False, True, False]

# # Definimos la función de simulación del DFA


# def simulate_dfa(input_string):
#     state = 0
#     for char in input_string:
#         if char == '/':
#             symbol = 0
#         elif char == '*':
#             symbol = 1
#         else:
#             symbol = 2
#         state = transition_table[state][symbol]
#     return accept_states[state]


# # Ejemplo de uso
# input_string = "/*a*/"
# print(simulate_dfa(input_string))  # Devuelve True

# input_string = "/**/a/*aa*/"
# print(simulate_dfa(input_string))  # Devuelve False
