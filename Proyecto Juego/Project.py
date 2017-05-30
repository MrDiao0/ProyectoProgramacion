from tkinter import *
import random
import time

h = []
i = 0
j = 0
k = 0
l = -160
m = -100
gas = 50
score = 0
def LvlsMenuS():
    """
    """
    def SPMenu(Track01):
        """
        """
        def SinglePlayer():
            # Crea la ventana y la asocia a la variable v
            ventana3.destroy()
            v = Tk()
            v.resizable(width=False,height=False)
            v.geometry("1475x720+0+0")
            v.config(cursor="cross")
            v.title("Road Fighter")
            
            ImgTrack=PhotoImage(file=Track01)
            ImgCar = PhotoImage(file="Textures/Vehicles/Runner/Runner.png")
            ImgCar2 = PhotoImage(file="Textures/Vehicles/Minivan/Minivan.png")
            ImgCar3 = PhotoImage(file="Textures/Vehicles/Fighter/Fighter.png")
            filename = PhotoImage(file="Textures/Vehicles/User/User.png")
            
            ImgScore=PhotoImage(file="Textures/Menu/InGame.png")

            
            
            presiono = False
            dx = None

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
                velocidadx1 = random.randint(0,1)
                def MoverRunner():
                    velocidady1 = random.randint(4,7)
                    if(d.coords(q)[1] <= 800 ):
                        
                        def MoveLeft():
                            if(d.coords(q)[0] > 390):
                                d.move(q,-5,velocidady1)
                                v.after(10,MoveLeft)
                            else:
                                MoveRight()
                        def MoveRight():
                            if(d.coords(q)[0] < 910):
                                d.move(q,5,velocidady1)
                                v.after(10,MoveRight)
                            else:
                                MoveLeft()
                        if(velocidadx1==1):
                            MoveRight()
                        else:
                            MoveLeft()
                    else:
                        d.delete(q)
                        return
                            
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


            def Gas():
                global gas
                if(gas>0):
                    gas = gas - 1
                    
                LblGas = Label(v,text = str(gas),bg="black",fg="white",font =("8bitoperator JVE",40)).place(x=1240,y=400)
                d.after(1000,Gas)

            def Score():
                global score
                score = score + 15
                
                LblGas = Label(v,text = str(score),bg="black",fg="white",font =("8bitoperator JVE",40)).place(x=1240,y=580)
                d.after(100,Score)
            # Crea los widgets
            d = Canvas(v, width=1475, height=720, )





            w = d.create_image(640,-5100,image=ImgTrack)

            d.bind("<KeyPress>",keydown)
            d.bind("<KeyRelease>",keyup)

            d.focus_set()

            
            d.pack()

            
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

            BG()
            key()
            Vehicles()
            Gas()
            Score()

            d.create_image(200,0,image=ImgScore,anchor=NW)

            LblPlayer1 = Label(v,text = Player1.get(),bg="black",fg="white",font =("8bitoperator JVE",40)).place(x=1240,y=80)
            
    
            v.mainloop()


        ventana2.destroy()
        ventana3=Tk()
        ventana3.geometry("1280x720+0+0")
        ventana3.config(cursor="cross")
        ventana3.title("Road Fighter")

        Player1 = StringVar()
        Player1.set("Player 1")
        Fondo=PhotoImage(file="Textures\Menu\SinglePlayer Menu\SinglePlayerName.png")
        label01=Label(ventana3,image=Fondo).place(x=0,y=0)

        #### Buttons ####
        imgBtnSPmenu=PhotoImage(file="Textures\Menu\SinglePlayer Menu\Play.png")
        btnSPMenu=Button(ventana3,width=150,height=75,image=imgBtnSPmenu,command=SinglePlayer).place(x=575,y=350)

        #### Entry ####
        txtPlayer1=Entry(ventana3,textvariable = Player1,font=("Arial",40),width=20).place(x=620,y=180)

        ventana3.mainloop()
    def Level11():
        """
        """
        Track01="Textures\Tracks\Level1\Track12.png"
        SPMenu(Track01)
    def Level21():
        """
        """
        Track01="Textures\Tracks\Level2\Track22.png"
        SPMenu(Track01)
    def Level31():
        """
        """
        Track01="Textures\Tracks\Level3\Track32.png"
        SPMenu(Track01)
    def Level41():
        """
        """
        Track01="Textures\Tracks\Level4\Track42.png"
        SPMenu(Track01)
    def Level51():
        """
        """
        Track01="Textures\Tracks\Level5\Track52.png"
        SPMenu(Track01)
    ventana1.destroy()
    
    #### Start Menu #####
    ventana2=Tk()
    ventana2.geometry("1280x720+0+0")
    ventana2.config(cursor="cross")
    ventana2.title("Road Fighter")

    imagen=PhotoImage(file="Textures\Menu\Levels Menu\LevelsMenu.png")
    lblimg0=Label(ventana2,image=imagen).place(x=0,y=0)

    #### Buttons Start Menu ####
    imgBtn1=PhotoImage(file="Textures\Menu\Levels Menu\Level 1.png")
    btn1=Button(ventana2,width=150,height=75,image=imgBtn1,command=Level11).place(x=450,y=200)

    imgBtn2=PhotoImage(file="Textures\Menu\Levels Menu\Level 2.png")
    btn2=Button(ventana2,width=150,height=75,image=imgBtn2,command=Level21).place(x=650,y=275)

    imgBtn3=PhotoImage(file="Textures\Menu\Levels Menu\Level 3.png")
    btn3=Button(ventana2,width=150,height=75,image=imgBtn3,command=Level31).place(x=450,y=350)

    imgBtn4=PhotoImage(file="Textures\Menu\Levels Menu\Level 4.png")
    btn4=Button(ventana2,width=150,height=75,image=imgBtn4,command=Level41).place(x=650,y=425)

    imgBtn5=PhotoImage(file="Textures\Menu\Levels Menu\Level 5.png")
    btn5=Button(ventana2,width=150,height=75,image=imgBtn5,command=Level51).place(x=450,y=500)
    
    ventana1.mainloop()

#=============================================================================================#

def LvlsMenuV():
    """
    """
    def VersusMenu():
        """
        """

        
        ventana2.destroy()
        
        ventana3=Tk()
        ventana3.geometry("1280x720+0+0")
        ventana3.config(cursor="cross")
        ventana3.title("Road Fighter")

        label01=Label(ventana3,text="intro to Tkinter").place(x=0,y=0)

        ImagenNV=PhotoImage(file="NamesVersus.png")

        label01=Label(ventana3,image=ImagenNV).place(x=0,y=0)

        #### Buttons ####
        imgBtnSPmenu=PhotoImage(file="Textures\Menu\Versus Menu\Play.png")
        btnSPMenu=Button(ventana3,width=150,height=75,image=imgBtnSPmenu).place(x=575,y=420)

        #### Text Box ####
        txtPlayer1=Entry(ventana3,font=("Arial",40),width=20).place(x=600,y=160)
        txtPlayer2=Entry(ventana3,font=("Arial",40),width=20).place(x=600,y=300)

        ventana3.mainloop()

    def Level12():
        """
        """
        ImgTrack=PhotoImage(file="Textures\Tracks\Level1\Track1.png")
        VersusMenu()
    def Level22():
        """
        """
        ImgTrack=PhotoImage(file="Textures\Tracks\Level2\Track2.png")
        VersusMenu()
    def Level32():
        """
        """
        ImgTrack=PhotoImage(file="Textures\Tracks\Level3\Track3.png")
        VersusMenu()
    def Level42():
        """
        """
        ImgTrack=PhotoImage(file="Textures\Tracks\Level4\Track4.png")
        VersusMenu()
    def Level52():
        """
        """
        ImgTrack=PhotoImage(file="Textures\Tracks\Level5\Track5.png")
        VersusMenu()
        
    ventana1.destroy()
    
    #### Start Menu #####
    ventana2=Tk()
    ventana2.geometry("1280x720+0+0")
    ventana2.config(cursor="cross")
    ventana2.title("Road Fighter")

    imagen=PhotoImage(file="Textures\Menu\Levels Menu\LevelsMenu.png")
    lblimg0=Label(ventana2,image=imagen).place(x=0,y=0)

    #### Buttons Start Menu ####
    imgBtn1=PhotoImage(file="Textures\Menu\Levels Menu\Level 1.png")
    btn1=Button(ventana2,width=150,height=75,image=imgBtn1,command=Level12).place(x=450,y=200)

    imgBtn2=PhotoImage(file="Textures\Menu\Levels Menu\Level 2.png")
    btn2=Button(ventana2,width=150,height=75,image=imgBtn2,command=Level22).place(x=650,y=275)

    imgBtn3=PhotoImage(file="Textures\Menu\Levels Menu\Level 3.png")
    btn3=Button(ventana2,width=150,height=75,image=imgBtn3,command=Level32).place(x=450,y=350)

    imgBtn4=PhotoImage(file="Textures\Menu\Levels Menu\Level 4.png")
    btn4=Button(ventana2,width=150,height=75,image=imgBtn4,command=Level42).place(x=650,y=425)

    imgBtn5=PhotoImage(file="Textures\Menu\Levels Menu\Level 5.png")
    btn5=Button(ventana2,width=150,height=75,image=imgBtn5,command=Level52).place(x=450,y=500)
    
    ventana1.mainloop()
    


def Exit():
    """
    """
    ventana1.destroy()
    exit()

#==================================================================================================#
def Instructions():
    """
    """
    v11 = Toplevel()
    v11.title("Instructions")
    v11.geometry("1280x720+0+0")
    instructions1 = PhotoImage(file="Textures\Menu\Instructions.gif")
    LabelInstructions = Label(v11,image=instructions1).place(x=0,y=0)
    
    def keyup(e):
        global h
        if(e.keycode in h):
            h.pop(h.index(e.keycode))

    def keydown(e):
        global h
        if not e.keycode in h:
            h.append(e.keycode)
                
    def key():
        global h
        if(13 in h):
            v11.destroy()
            h.pop(0)
        v11.after(10,key)


    v11.bind("<KeyPress>",keydown)
    v11.bind("<KeyRelease>",keyup)

    key()
    
    v11.mainloop()
        
#==================================================================================================#
    
#### Start Menu #####
ventana1=Tk()
ventana1.geometry("1280x720+0+0")

ventana1.title("Road Fighter")

imagen=PhotoImage(file="Textures\Menu\Start Menu\StartMenu.png")
lblimg=Label(ventana1,image=imagen).place(x=0,y=0)

#### Buttons Start Menu ####
imgBtnSP=PhotoImage(file="Textures\Menu\Start Menu\Buttons\SinglePlayer.png")
btnSP=Button(ventana1,width=150,height=75,image=imgBtnSP,command=LvlsMenuS).place(x=575,y=300)

imgBtnVersus=PhotoImage(file="Textures\Menu\Start Menu\Buttons\Versus.png")
btnVersus=Button(ventana1,width=150,height=75,image=imgBtnVersus,command=LvlsMenuV).place(x=575,y=400)

imgBtnExit=PhotoImage(file="Textures\Menu\Start Menu\Buttons\Exit.png")
btnExit=Button(ventana1,width=150,height=75,image=imgBtnExit,command=Exit).place(x=575,y=500)

Menu0=Menu(ventana1)
Barra=Menu(ventana1)
Menu0.add_command(label="Instructions",command=Instructions)
Barra.add_cascade(label="Archivo",menu=Menu0)

ventana1.config(cursor="cross",menu=Barra)
ventana1.resizable(width=False,height=False)

ventana1.mainloop()

#==================================================================================================#
