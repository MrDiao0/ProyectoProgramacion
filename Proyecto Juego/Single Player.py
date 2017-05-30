from tkinter import *
import time
import random

# Crea la ventana y la asocia a la variable v
v = Tk()
v.resizable(width=False,height=False)
v.geometry("1475x720+0+0")
v.config(cursor="cross")
v.title("Road Fighter")

ImgCar = PhotoImage(file="Runner.png")
ImgCar2 = PhotoImage(file="Minivan.png")
ImgCar3 = PhotoImage(file="Fighter.png")

ImgScore=PhotoImage(file="InGame.png")
ImgTrack=PhotoImage(file="Track12.png")
h = []
presiono = False
dx = None
i = 0
j = 0
k = 0
l = -160
m = -100

def BG():
    """
    """
    
    d.move(w,0,5)
    v.after(5,BG)

def Fighter():
    FighterX = random.randint(390,910)
    q2 = d.create_image(FighterX,-87,image=ImgCar3)
    def MoverFighter():
        velocidady3 = random.randint(2,4)
        if(d.coords(q2)[1] <= 800):
            if(d.coords(q2)[0] > d.coords(x)[0]):
                d.move(q2,-2,velocidady3)
            if(d.coords(q2)[0] < d.coords(x)[0]):
                d.move(q2,2,velocidady3)
            if(d.coords(q2)[0] == d.coords(x)[0]):
                d.move(q2,0,velocidady3)
        else:
            d.delete(q2)
            return
        v.after(10,MoverFighter)
    MoverFighter()
    
def Runner():
    RunnerX = random.randint(390,910)
    q = d.create_image(RunnerX,-87,image=ImgCar)
    
    def MoverRunner():
        velocidady1 = random.randint(4,7)
        velocidadx1 = random.randint(-2,1)
        if(d.coords(q)[1] <= 800 ):
            if(d.coords(q)[0] <= 910 and d.coords(q)[0] >= 390):
                if(velocidadx1 < 0):
                    d.move(q,-5,velocidady1)
                if(velocidadx1 >= 0):
                    d.move(q,5,velocidady1)
            else:
                d.move(q,0,velocidady1)
        else:
            d.delete(q)
            return
                
        v.after(10,MoverRunner)
    MoverRunner()


def Minivan():
    MinivanX = random.randint(390,910)
    q1 = d.create_image(MinivanX,-87,image=ImgCar2)
    def MoverMinivan():
        velocidady2 = random.randint(4,7)
        if(d.coords(q1)[1] <= 800 ):
            d.move(q1,0,velocidady2)
        else:
            d.delete(q1)
            return
        v.after(10,MoverMinivan)
    MoverMinivan()

def keyup(e):
  global h
  if(e.keycode in h):
    h.pop(h.index(e.keycode))

def keydown(e):
  global h
  if not e.keycode in h:
    h.append(e.keycode)
    
def key():
    """
    """
    global h,i
    if(68 in h):
        if(i < 350):
            i = i + 10
            d.move(x,7,0)
    if(65 in h):
        if(i > -350):
            i = i - 10
            d.move(x,-7,0)
    d.after(15,key)




     
# Crea los widgets
d = Canvas(v, width=1475, height=720, )





w = d.create_image(640,-5100,image=ImgTrack)

d.bind("<KeyPress>",keydown)
d.bind("<KeyRelease>",keyup)

d.focus_set()

BG()
d.pack()

filename = PhotoImage(file="User.png")
x = d.create_image(650,620,image=filename)


def Vehicles():
    RandomV = random.randint(0,300)
    if(RandomV == 0):
        Minivan()
    if(RandomV == 1):
        Runner()
    if(RandomV == 2):
        Fighter()

    v.after(10,Vehicles)
key()
Vehicles()


d.create_image(200,0,image=ImgScore,anchor=NW)
v.mainloop()
