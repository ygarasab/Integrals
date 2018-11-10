from random import uniform
import os
from math import *


class Integrador:

    def __init__(self):

        self.f = 0
        self.run = 1

        while self.run: self.menu()

    def menu(self):

        os.system('cls')
        print('\n[Integrador v0.2]\n')

        if not self.f:
            print("\n> Vamos começar do começo, me dê a função que você deseja integrar\n")
            self.fun = input("< ")
            if self.n_fun():
                self.limites()
                return
            else:
                print('> Parece que você não me deu uma função válida')
                input()
                return
        self.limites()

    def n_fun(self):
        try:
            x = "def f(x): return "+ self.fun
            k = "self.f=f"
            exec(x)
            exec(k)
            self.fun = 'f(x) = '+self.fun
            return 1
        except: return 0


    def limites(self):

        print("\n\n> Defina o limite inferior para a integração da função %s."%self.fun)
        print("> Digite um valor não numérico para definir outra função.\n")

        x = input("< ")
        self.limI = 0
        try:
            exec("self.limI="+x)
            float(self.limI)
        except:
            self.f = 0
            return

        print("\n> Agora, o limite de integração superior.\n")
        x = input("< ")
        self.limS = 0
        try:
            exec("self.limS=" + x)
            float(self.limS)
        except:
            self.f = 0
            return

        self.delta = self.limS - self.limI

        print('\n> Tudo certo. Vamos Integrar!')

        try: self.integrate()
        except:
            print("\n> Ocorreu um erro durante a integração.\n> Verifique se a função está correta e se os limites de integração são válidos.")
            input()

    def integrate(self):

        f = self.f

        ps = [f(self.limI+(self.delta/10)*i) for i in range(10)]
        h = max(ps)+1

        a = self.delta * h

        k = 100000

        dentro = 0
        fora = 0

        xi = [uniform(self.limI, self.limS) for i in range(k)]
        yi = [uniform(0, h) for i in range(k)]

        for i in range(k):
            if yi[i] <= f(xi[i]):
                dentro += 1
            else:
                fora += 1
        print("\n\n> Com %d pontos criados, eu acho que o resultado da sua integração resultar em algo próximo de"%k,(dentro/k)* a)
        input()


Integrador()