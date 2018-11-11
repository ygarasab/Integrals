from math import *
from random import uniform

fun = input("Digite sua função: ")
fun = "def f(x): return "+ fun

exec(fun)

l_i = input("Digite o limite inferior: ")
x = "l_i = "+l_i
exec(x)

l_s = input("Digite o limite superior: ")
x = "l_s = "+l_s
exec(x)

ps = [f(l_i+((l_s-l_i)/10)*i) for i in range(0,11)]

h = max(ps)+1

k = 100000

x = [uniform(l_i,l_s) for i in range(k)]
y = [uniform(0, h) for i in range(k)]

dentro = 0
fora = 0

for i in range(k):
    if y[i]<=f(x[i]): dentro+=1
    else: fora+=1

prcent = dentro/k
integral = prcent*(l_s-l_i)*h

print(integral)