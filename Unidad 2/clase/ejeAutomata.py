
"""
def KTransitionTable(kNumStates, kNumSymbols):
    list_symbols = [[1,0],[3,2],[3,0],[3,3]]

def KAcceptTable(kNumStates):
    list_states= [True, False,False, True] 

def simulateDFA(input):
    state=0
    for c in input:
        state = KTransitionTable(state,c)
    return KAcceptTable(state)
"""


# 33
# KTransitionTable = [[1,0],[3,2],[3,0],[3,3]]

# KAcceptTable= [True,False,False, True]

# def simulateDFA(input):
#     state=0
#     n=0

#     for c in input:
#         if n >1:
#             n=0
#         state = KTransitionTable[state][n]

#         n+=1
#     #print("uno")
#     return KAcceptTable[state]
# string="1"
# print(simulateDFA(string))

"""Codigo en clase"""

# # Definimos la tabla de transiciones
# transition_table = [[1, 0], [3, 2], [3, 0], [3, 3]]

# # Definimos la lista de estados finales
# accept_states = [True, False, False, True]

# # Definimos la función de simulación del DFA


# def simulate_dfa(input_string):
#     state = 0
#     for char in input_string:
#         symbol = int(char)  # Convertimos el caracter a un número entero
#         state = transition_table[state][symbol]
#     return accept_states[state]


# # Ejemplo de uso
# input_string = "101101"
# print(simulate_dfa(input_string))  # Devuelve True


"""Actividad Extraordinaria"""
"""
Let's design a DFA for C-style comments. Those are the ones that start with /* and end with */.
Accepted:
/*a*/
/**/
/***/
/*aaa*aaa*/
/*a/a*/
Rejected:
/**
/**/a/*aa*/
aaa/**/aa
/*/
/**a/
//aaaa
"""


"""
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
"""


"""
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
"""


"""
    /   a   *
q0  q1  q5  q5
q1  q5  q5  q2
q2  q2  q2  q3
q3  q4  q2  q3
q4  Σ   Σ   Σ
q5  Σ   Σ   Σ

"""


"""
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
"""
