# # Definición del DFA
# dfa = {
#     0: {'/': 1, 'a': 4, '*': 7},
#     1: {'*': 2},
#     2: {'*': 2, '/': 3},
#     3: {},
#     4: {'/': 5, 'a': 4, '*': 7},
#     5: {},
#     6: {},
#     7: {'/': 8, 'a': 7, '*': 6},
#     8: {}
# }

# # Definición de los estados de aceptación
# aceptacion = {3, 5, 8}

# # Función que verifica si una cadena es aceptada por el DFA


# def simulateDFA(input):
#     state = 0
#     for c in input:
#         if c not in dfa[state]:
#             return False
#         state = dfa[state][c]
#     return state in aceptacion


# print(simulateDFA("/*a*/"))
# print(simulateDFA("/***/"))
# print(simulateDFA("/*aaa*aaa*/"))
# print(simulateDFA("/*a/a*/"))

# print(simulateDFA("/**/a/*aa*/"))
# print(simulateDFA("aaa/**/aa"))
# print(simulateDFA("/*/"))
# print(simulateDFA("/**a/"))
# print(simulateDFA("//aaaa"))
