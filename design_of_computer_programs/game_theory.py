
import math

million = 1000000

def Q(state, action, U):
    if action == 'hold':
        return U(state + 1*million)
    if action == 'gamble':
        return U(state + 3*million)*.5 + U(state) * 0.5

U = math.log10
c = 1 * million

print(Q(c,'hold', U))
print(Q(c,'gamble', U))
