from tkinter import *
from PIL import Image, ImageTk
from turtle import *
from math import *
from random import uniform

class App(Frame):

    def __init__(self, master= None):
        master.title("Integrals")
        master.geometry("1000x600")

        Frame.__init__(self, master)

        self.master = master
        self["bg"] = 'white'

        self.window()

    def clear(self):

        for i in self.l:
            i.destroy()

    def window(self):

        self.pack(fill=BOTH, expand=1)

        load = Image.open("icon.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image = render)
        img.image = render
        img["bg"]='white'
        img.pack(pady=60)

        welcome = Label(self, text="Integrador Montecarlo", font=("Arial", 30))
        welcome["bg"] = 'white'
        welcome.pack()

        iniciar = Button(self,text='Nova Integração', cursor="hand2", height=3, width=20,command=self.new)

        iniciar.pack(pady=20)

        self.l=[img, welcome, iniciar]

    def cartesiano(self):
        t = RawTurtle(self.canvas)
        t.penup()
        t.setposition(-310, -260)
        t.left(90)
        t.pendown()
        t.forward(520)
        t.stamp()

        t.penup()
        t.setposition(-310, -260)
        t.right(90)
        t.pendown()
        t.forward(600)
        t.stamp()



    def new(self):

        self.clear()

        self.canvas = Canvas(self, width=700, height=600)
        self.canvas.pack(side=LEFT)



        self.right = Frame(self, bg='white', height=80,width=100)
        self.right.pack(side=TOP, fill=BOTH, pady=70, expand=1)

        self.lbl = Label(self.right, font=("Arial", 12), bg='white')
        self.lbl.pack(pady=40)

        self.e = Entry(self.right,bd=2, width=40, justify=CENTER)
        self.e.pack()

        self.get_fun(0)

    def get_fun(self,x):

        v = self.e.get()
        self.e.delete(0,END)

        if not( x or v ):
            self.lbl['text'] = "Qual função deseja integrar?"
            self.e.bind('<Return>', self.get_fun)
        else:
            try:
                x = "def f(x):\n try: return "+ v +"\n except: return 0"
                t = "f(4)"
                k = "self.f=f"
                print(x)
                exec(x)
                exec(t)
                exec(k)

                self.fun = "f(x) = "+v

                y = 0

            except: y = 1

            if y: self.get_fun(0)
            else:
                self.fun_str = "f(x) = "+v
                self.fun_lbl = Label(self.right,text=self.fun_str, bg='white', font=('Arial, 11'),anchor=W)

                self.get_limits(0)

    def get_limits(self,w):
        v = self.e.get()
        self.e.delete(0,END)
        self.e.unbind('<Return>')

        if not( w or v ):
            self.lbl['text'] = "Insira os limites inferior e superior\nseparados por espaço"
            self.e.bind('<Return>', self.get_limits)
        else:
            l = v.split()
            self.ls =[0,0]
            print(l)

            for i in range(2):

                try:
                    q = "self.ls[%d]="%i
                    exec(q + l[i])
                    float(self.ls[i])
                except:
                    print('erro')
            self.lbl.destroy()
            self.e.destroy()
            self.lim_lbl = Label(self.right,text='de {} a {}'.format(*self.ls), bg='white', font=('Arial, 11'),anchor=W)
            self.lim_lbl.pack(padx=30, side=BOTTOM, fill=BOTH)
            self.fun_lbl.pack(padx=30, side=BOTTOM, fill=BOTH)
            self.draw()


    def parar(self):

        self.para = 1


    def draw(self):

        self.lbl = Label(self.right,text='Integrando', font = ('Arial', 30), bg='white', anchor=W)
        self.lbl.pack(fill=BOTH, padx=30)

        self.cartesiano()

        fim = 1.2*self.ls[1]
        px = fim / 600

        self.h = max(self.f(px),self.f(self.ls[0]), self.f(self.ls[1]), self.f(fim))


        propy = 520/(1.2*self.h)
        print(propy)
        zero = -310

        t = RawTurtle(self.canvas)
        t.shapesize(.1)
        t.penup()
        t.shape('circle')
        t.setposition(-310, -260)
        t.pendown()
        t.speed(0)
        self.lbl0 = Label(self.right,text='Pontos criados = 0')
        self.lbl1 = Label(self.right, text='Pontos dentro = 0')
        self.lbl2 = Label(self.right, text='Pontos fora = 0')
        self.lbl3 = Label(self.right, text='Integral estimada = 0')
        l = [self.lbl0,self.lbl1,self.lbl2,self.lbl3]
        for i in l:
            i['anchor'] = W
            i.pack(fill=BOTH, padx=30, pady=5)
            i['bg'] = 'white'
        self.ins = 0
        self.out = 0

        self.a = (self.ls[1]-self.ls[0])*self.h

        t.color('red')
        for i in range(0,600):
            x = zero + i
            y = -260+self.f(i*px)*propy
            t.setposition(x,y)
        t.color('black')
        k=10000
        xi = [uniform(self.ls[0], self.ls[1]) for i in range(k)]
        yi = [uniform(0, self.h) for i in range(k)]
        t.shapesize(.2)
        t.penup()

        self.para = 0

        self.st = Button(self.right,text='Parar',command = self.parar, width=6, height=2)
        self.st.pack(side= LEFT, padx=30)

        for i in range(1,k+1):

            if self.para: break;

            f = self.f(xi[i])
            t.setposition(zero+xi[i]/px, -260+yi[i]*propy)
            t.stamp()
            if yi[i] <= f:
                self.ins += 1
            else:
                self.out += 1
            self.lbl0['text'] = 'Pontos criados = %d'%i
            self.lbl1['text'] = 'Pontos dentro = %d' %self.ins
            self.lbl2['text'] = 'Pontos fora = %d' %self.out
            self.lbl3['text'] = 'Integral estimada = %.2f' %((self.ins/i)*self.a)










root  = Tk()
app = App(master=root)
app.mainloop()