from tkinter import *
from PIL import Image, ImageTk
from turtle import *
from math import *

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
        t.setposition(-260, -260)
        t.left(90)
        t.pendown()
        t.forward(520)
        t.stamp()

        t.penup()
        t.setposition(-280, -200)
        t.right(90)
        t.pendown()
        t.forward(520)
        t.stamp()



    def new(self):

        self.clear()

        self.canvas = Canvas(self, width=600, height=600)
        self.canvas.pack(side=LEFT)

        self.right = Frame(self, bg = 'white')
        self.right.pack(side=TOP, pady=150)

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
                x = "def f(x): return "+ v
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
            else: self.get_limits(0)

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

            print(self.ls)





root  = Tk()
app = App(master=root)
app.mainloop()