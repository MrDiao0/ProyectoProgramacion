from tkinter import *
import random,time

#Conjunto en el que se encuentran las teclas presionadas
h = []

#Valor de la gasolina para el modo un jugador
gas = 75


#Gasolina jugador 1 en modo versus
gas1 = 75
#Gasolina jugador 2 en modo versus
gas2 = 75

#Velocidad de la pista para un jugador y para el jugador 1 en el modo versus
MaxS = 0
#Velocidad de la pista para el jugador 2 en modo versus
MaxS2 = 0

#Puntaje para el modo un jugador
score = 0

#Puntaje para el jugador 1 en modo versus
score1 = 0
#Puntaje para el jugador 2 en modo versus
score2 = 0

#Velocidad del vehiculo del Usuario
SpeedC = 0
#Velocidad del vehiculo en el label
SpeedC1 = 0
#Velocidad del Vehiculo en el label modo versus
SpeedC2 = 0

#Velocidad de los vehiculos generados aleatoriamente
SpeedV = 0

#Indice de aparicion de Vehiculos enemigos
SpawnV = 0
#Indice de aparicion de items(power-ups) 
SpawnP = 0

#Afirma cuando el jugador 1 acabo con su gasolina o perdio
Player1W = True
#Afirma cuando el jugador 1 acabo con su gasolina o perdio
Player2W = True

#Velocidad de cada vehiculo individualmente en el eje Y, la cual puede variar
velocidady2 = 0

#Velocidad para el vehiculo runner la cual varia constantemente
velocidadx1 = 0

#========================================ONE PLAYER==================================================#
def LvlsMenuS():
    """
    """

    def SPMenu(Track01):
        """
        """
        def SinglePlayer():
            """
            Funcion principal para el modo un jugador
            """
    
            # Crea la ventana y la asocia a la variable v
            global window
            ventana3.destroy()
            window = True
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

            ImgGas = PhotoImage(file="Textures/PowerUps/Gas.png")
            ImgOil = PhotoImage(file="Textures/PowerUps/Oil.png")
            ImgScore = PhotoImage(file="Textures/Menu/InGame.png")

            

            def BG():
                """
                Mueve la carretera dependiendo de la velocidad del nivel
                """
                global MaxS
                d.move(w,0,MaxS)
                v.after(10,BG)
                    

            def Fighter():
                """
                Funcion principal para la generacion del vehiculo: Fighter
                """
                FighterX = random.randint(390,910)
                q2 = d.create_image(FighterX,-87,image=ImgCar3)
                def MoverFighter():
                    """
                    Funcion la cual mueve el vehiculo: Fighter, dependiendo de la velocidad dada por el nivel
                    """
                    global gas,MaxS,SpeedV,score,SpeedC1
                    posx22 = d.coords(q2)[0]
                    posy22 = d.coords(q2)[1]
                    posx11 = d.coords(x)[0]
                    posy11 = d.coords(x)[1]
                    
                    velocidady3 = random.randint(2,SpeedV)
                    if(d.coords(q2)[1] <= 800):
                        if(d.coords(q2)[0] > d.coords(x)[0]):
                            d.move(q2,-2,velocidady3)
                        if(d.coords(q2)[0] < d.coords(x)[0]):
                            d.move(q2,2,velocidady3)
                        if(d.coords(q2)[0] == d.coords(x)[0]):
                            d.move(q2,0,velocidady3)
                            
                        if(posx11 >= posx22 and posx11 <= posx22 + 49 and posy11 >= posy22 and posy11 <= posy22 + 160):
                            gas = gas - 10
                            score = score -20
                            SpeedC1 = SpeedC1-15
                            d.delete(q2)
                            return
                        if(posx11 <= posx22 and posx11 - 49 >= posx22 and posy11 <= posy22 and posy11 + 160 <= posy22):
                            gas = gas - 10
                            score = score -20
                            SpeedC1 = SpeedC1-15
                            d.delete(q2)
                            return
                        
                            
                    else:
                        d.delete(q2)
                        return
                    if(MaxS != 0):
                        v.after(10,MoverFighter)
                MoverFighter()
                
            def Runner():
                """
                Funcion principal para la generacion del vehiculo: Runner
                """
                RunnerX = random.randint(390,910)
                q = d.create_image(RunnerX,-87,image=ImgCar)
                velocidadx1 = random.randint(0,1)
                def MoverRunner():
                    """
                    Funcion la cual mueve el vehiculo: Fighter, dependiendo de la velocidad dada por el nivel
                    """
                    global gas,MaxS,SpeedV,score
                    
                    velocidady1 = random.randint(4,SpeedV)
                    if(d.coords(q)[1] <= 800 ):
                        
                        def MoveLeft():
                            """
                            Funcion la cual mueve el vehiculo Runner hacia el lado izquierdo
                            """
                            global gas,MaxS,SpeedV,score,SpeedC1
                            posx22 = d.coords(q)[0]
                            posy22 = d.coords(q)[1]
                            posx11 = d.coords(x)[0]
                            posy11 = d.coords(x)[1]
                            if(posx11 >= posx22 and posx11 <= posx22 + 49 and posy11 >= posy22 and posy11 <= posy22 + 160):
                                gas = gas - 10
                                score = score -20
                                SpeedC1 = SpeedC1-15
                                d.delete(q)
                                return
                            if(posx11 <= posx22 and posx11 + 49 >= posx22 and posy11 <= posy22 and posy11 + 160 <= posy22):
                                gas = gas - 10
                                score = score -20
                                SpeedC1 = SpeedC1-15
                                d.delete(q)
                                return
                            if(posx11 <= posx22 and posx11 >= posx22 - 49 and posy11 <= posy22 and posy11 >= posy22 - 160):
                                gas = gas - 10
                                score = score -20
                                SpeedC1 = SpeedC1-15
                                d.delete(q)
                                return
                            if(posx11 >= posx22 and posx11 + 49 <= posx22 and posy11 >= posy22 and posy11 + 160 >= posy22):
                                gas = gas - 10
                                score = score - 20
                                SpeedC1 = SpeedC1-15
                                d.delete(q)
                                return
                            if(d.coords(q)[0] > 390):
                                d.move(q,-5,velocidady1)
                                if(MaxS != 0):
                                    v.after(10,MoveLeft)
                            else:
                                MoveRight()
                        def MoveRight():
                            """
                            Funcion la cual mueve el vehiculo Runner hacia el lado derecho
                            """
                            global gas,MaxS,SpeedV,score,SpeedC1
                            posx22 = d.coords(q)[0]
                            posy22 = d.coords(q)[1]
                            posx11 = d.coords(x)[0]
                            posy11 = d.coords(x)[1]
                            if(posx11 >= posx22 and posx11 <= posx22 + 49 and posy11 >= posy22 and posy11 <= posy22 + 160):
                                gas = gas - 10
                                score = score -20
                                SpeedC1 = SpeedC1-15
                                d.delete(q)
                                return
                            if(posx11 <= posx22 and posx11 + 49 >= posx22 and posy11 <= posy22 and posy11 + 160 <= posy22):
                                gas = gas - 10
                                score = score -20
                                SpeedC1 = SpeedC1-15
                                d.delete(q)
                                return
                            if(posx11 <= posx22 and posx11 >= posx22 - 49 and posy11 <= posy22 and posy11 >= posy22 - 160):
                                gas = gas - 10
                                score = score -20
                                SpeedC1 = SpeedC1-15
                                d.delete(q)
                                return
                            if(posx11 >= posx22 and posx11 + 49 <= posx22 and posy11 >= posy22 and posy11 + 160 >= posy22):
                                gas = gas - 10
                                score = score -20
                                SpeedC1 = SpeedC1-15
                                d.delete(q)
                                return
                            if(d.coords(q)[0] < 910):
                                d.move(q,5,velocidady1)
                                if(MaxS != 0):
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
                """
                Funcion principal para la generacion del vehiculo: Minivan
                """
                MinivanX = random.randint(390,910)
                q1 = d.create_image(MinivanX,-87,image=ImgCar2)
                def MoverMinivan():
                    """
                    Funcion la cual mueve el vehiculo: Fighter, dependiendo de la velocidad dada por el nivel
                    """
                    global gas,MaxS,SpeedV,score,SpeedC1
                    posx22 = d.coords(q1)[0]
                    posy22 = d.coords(q1)[1]
                    posx11 = d.coords(x)[0]
                    posy11 = d.coords(x)[1]
                    
                    velocidady2 = random.randint(4,SpeedV)
                    if(d.coords(q1)[1] <= 800 ):
                        d.move(q1,0,velocidady2)
                        if(posx11 >= posx22 and posx11 <= posx22 + 49 and posy11 >= posy22 and posy11 <= posy22 + 160):
                            gas = gas - 10
                            score = score -20
                            SpeedC1 = SpeedC1-15
                            d.move(q1,0,1000)
                        if(posx11 <= posx22 and posx11 + 49 >= posx22 and posy11 <= posy22 and posy11 + 160 <= posy22):
                            gas = gas - 10
                            score = score -20
                            SpeedC1 = SpeedC1-15
                            d.move(q1,0,1000)
                        if(posx11 <= posx22 and posx11 >= posx22 - 49 and posy11 <= posy22 and posy11 >= posy22 - 160):
                            gas = gas - 10
                            score = score -20
                            SpeedC1 = SpeedC1-15
                            d.move(q1,0,1000)
                        if(posx11 >= posx22 and posx11 + 49 <= posx22 and posy11 >= posy22 and posy11 + 160 >= posy22):
                            gas = gas - 10
                            score = score -20
                            SpeedC1 = SpeedC1-15
                            d.move(q1,0,1000)
                    
                    else:
                        d.delete(q1)
                        return
                    
                    if(MaxS != 0):
                        v.after(10,MoverMinivan)
                MoverMinivan()

            def PowerGas():
                """
                Funcion principal para la generacion del item: Gasolina
                """
                GasX = random.randint(390,910)
                q1 = d.create_image(GasX,-87,image=ImgGas)
                def MoveGas():
                    """
                    Funcion la cual mueve el item: Gasolina
                    """
                    global gas,MaxS,score
                    posx22 = d.coords(q1)[0]
                    posy22 = d.coords(q1)[1]
                    posx11 = d.coords(x)[0]
                    posy11 = d.coords(x)[1]
                    
                    if(d.coords(q1)[1] <= 800 ):
                        d.move(q1,0,7)
                        if(posx11 >= posx22 and posx11 <= posx22 + 49 and posy11 >= posy22 and posy11 <= posy22 + 160):
                            gas = gas + 20
                            score = score + 15
                            d.move(q1,0,1000)
                        if(posx11 <= posx22 and posx11 + 49 >= posx22 and posy11 <= posy22 and posy11 + 160 <= posy22):
                            gas = gas + 20
                            score = score + 15
                            d.move(q1,0,1000)
                        if(posx11 <= posx22 and posx11 >= posx22 - 49 and posy11 <= posy22 and posy11 >= posy22 - 160):
                            gas = gas + 20
                            score = score + 15
                            d.move(q1,0,1000)
                        if(posx11 >= posx22 and posx11 + 49 <= posx22 and posy11 >= posy22 and posy11 + 160 >= posy22):
                            gas = gas + 20
                            score = score + 15
                            d.move(q1,0,1000)
                    
                    else:
                        d.delete(q1)
                        return
                    
                    if(MaxS != 0):
                        v.after(10,MoveGas)
                MoveGas()

            def Oil():
                """
                Funcion principal para la generacion del item: Aceite
                """
                OilX = random.randint(390,910)
                q1 = d.create_image(OilX,-87,image=ImgOil)
                def MoveOil():
                    """
                    Funcion la cual mueve el item: Aceite
                    """
                    global MaxS,SpeedC1
                    posx22 = d.coords(q1)[0]
                    posy22 = d.coords(q1)[1]
                    posx11 = d.coords(x)[0]
                    posy11 = d.coords(x)[1]

                    if(d.coords(q1)[1] <= 800 ):
                        d.move(q1,0,MaxS)

                        if(posx22 <= 650):
                            if(posx11 >= posx22 and posx11 <= posx22 + 49 and posy11 >= posy22 and posy11 <= posy22 + 160):
                                d.move(x,30,0)
                                SpeedC1 = SpeedC1-5
                            if(posx11 <= posx22 and posx11 + 49 >= posx22 and posy11 <= posy22 and posy11 + 160 <= posy22):
                                d.move(x,30,0)
                                SpeedC1 = SpeedC1-5
                            if(posx11 <= posx22 and posx11 >= posx22 - 49 and posy11 <= posy22 and posy11 >= posy22 - 160):
                                d.move(x,30,0)
                                SpeedC1 = SpeedC1-5
                            if(posx11 >= posx22 and posx11 + 49 <= posx22 and posy11 >= posy22 and posy11 + 160 >= posy22):
                                d.move(x,30,0)
                                SpeedC1 = SpeedC1-5
                        if(posx22 > 650):
                            if(posx11 >= posx22 and posx11 <= posx22 + 49 and posy11 >= posy22 and posy11 <= posy22 + 160):
                                d.move(x,-30,0)
                                SpeedC1 = SpeedC1-5
                            if(posx11 <= posx22 and posx11 + 49 >= posx22 and posy11 <= posy22 and posy11 + 160 <= posy22):
                                d.move(x,-30,0)
                                SpeedC1 = SpeedC1-5
                            if(posx11 <= posx22 and posx11 >= posx22 - 49 and posy11 <= posy22 and posy11 >= posy22 - 160):
                                d.move(x,-30,0)
                                SpeedC1 = SpeedC1-5
                            if(posx11 >= posx22 and posx11 + 49 <= posx22 and posy11 >= posy22 and posy11 + 160 >= posy22):
                                d.move(x,-30,0)
                                SpeedC1 = SpeedC1-5
                    
                    else:
                        d.delete(q1)
                        return
                    if(MaxS != 0):
                        v.after(10,MoveOil)
                MoveOil()
                
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
                Funcion que genera movimiento a base presionar ciertas teclas determinadas por el usuario
                """
                global h,SpeedC
                if(68 in h):
                    if(d.coords(x)[0] < 890):
                        d.move(x,SpeedC,0)
                if(65 in h):
                    if(d.coords(x)[0] > 405):
                        d.move(x,-(SpeedC),0)
                if(MaxS !=0):
                    d.after(15,key)
            def exitt():
                exit()

            def Gas():
                """
                Funcion la cual define y cambia el item: Gasolina y lo muestra en un Label
                """
                global gas,MaxS
                LblGas = Label(v,text = gas,bg="black",fg="white",font =("8bitoperator JVE",40)).place(x=1240,y=400)
                d.delete(LblGas)
                if(gas>0):
                    gas = gas - 1
                if(gas<=0):
                    gas = 0
                    MaxS = 0
                    LblGas = Label(v,text ="00",bg="black",fg="white",font =("8bitoperator JVE",40)).place(x=1240,y=400)
                    LblOutGas = Label(v,text = "OUT OF GAS :(",bg="black",fg="white",font =("8bitoperator JVE",100)).place(x=200,y=300)
                    d.after(2000,exitt)
                    
                d.after(500,Gas)

            def Score():
                """
                Funcion la cual define y cambia el item: Puntaje y lo muestra en un Label
                """
                global score
                if(MaxS != 0):
                    score = score + 15
                
                LblGas = Label(v,text = str(score),bg="black",fg="white",font =("8bitoperator JVE",40)).place(x=1240,y=580)
                d.after(100,Score)
            # Crea los widgets
            d = Canvas(v, width=1475, height=720, )


            def Victory():
                """
                Funcion la cual despues de sobrevivir 60 segundos, muestra la victoria del jugador
                """
                global MaxS
                if(MaxS != 0):
                    MaxS = 0
                    LblWin = Label(v,text = "YOU WIN :')",bg="black",fg="white",font =("8bitoperator JVE",100)).place(x=200,y=300)
                    if(Track01 == "Textures\Tracks\Level1\Track52.png"):
                        d.delete(LblWin)
                        LblGas = Label(v,text = "THE END...?",bg="black",fg="white",font =("8bitoperator JVE",100)).place(x=200,y=300)
                    d.after(2000,exitt)

            def Speed():
                """
                Funcion la cual muestra en un label la velocidad a la que va el usuario
                """
                global SpeedC,SpeedC1,MaxS
                if(MaxS !=0):
                    if(Track01 == "Textures\Tracks\Level5\Track52.png"):
                        LblSpeed = Label(d,text = "Speed: 999",bg="black",fg="white",font=("8bitoperator JVE",40)).place(x=1220,y=240)
                    else:
                        if(SpeedC1 < int((SpeedC*100)/3)):
                            SpeedC1 = SpeedC1 + 1
                        LblSpeed = Label(d,text = "Speed: " + str(SpeedC1) ,bg="black",fg="white",font=("8bitoperator JVE",40)).place(x=1220,y=240)
                        d.delete(LblSpeed)
                else:
                    LblSpeed = Label(d,text = "Speed: 000",bg="black",fg="white",font=("8bitoperator JVE",40)).place(x=1220,y=240)
                d.after(200,Speed)
                        
            w = d.create_image(640,-10200,image=ImgTrack)

            d.bind("<KeyPress>",keydown)
            d.bind("<KeyRelease>",keyup)

            d.focus_set()

            
            d.pack()

            
            x = d.create_image(650,620,image=filename)


            def Randoms():
                """
                Funcion la se encarga de generar items y vehiculos de manera aleatoria y en posiciones aleatorias
                """
                global SpawnV,SpawnP
                RandomV = random.randint(0,SpawnV)
                if(RandomV == 0 and MaxS !=0):
                    Minivan()
                if(RandomV == 1 and MaxS !=0):
                    Runner()
                if(RandomV == 2 and MaxS !=0):
                    Fighter()
                RandomG = random.randint(0,SpawnP)
                if(RandomG == 250 and MaxS !=0):
                    PowerGas()
                if(RandomG == 150 and MaxS !=0):
                    Oil()
                v.after(10,Randoms)

            #============Se cargan todos los elementos=============#
            BG()
            key()
            Randoms()
            Gas()
            Score()
            Speed()
            d.after(60000,Victory)
            #======================================================#
            
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
        txtPlayer1=Entry(ventana3,textvariable = Player1,font=("8bitoperator JVE",40),width=20).place(x=620,y=180)

        ventana3.mainloop()
    def Level11():
        """
        Funcion la cual le da la velocidad a los velhiculos, el indice de aparicion de items y vehiculos y carga la imagen del Mapa
        """
        global MaxS,SpawnV,SpawnP,SpeedC,SpeedV,SpeedC1
        MaxS = 4
        SpawnV = 500
        SpawnP = 600
        SpeedC = 7
        SpeedC1 = int((SpeedC*100)/3)
        SpeedV = 7
        Track01="Textures\Tracks\Level1\Track12.png"
        SPMenu(Track01)
    def Level21():
        """
        Funcion la cual le da la velocidad a los velhiculos, el indice de aparicion de items y vehiculos y carga la imagen del Mapa
        """
        global MaxS,SpawnV,SpawnP,SpeedC,SpeedV,SpeedC1
        MaxS = 6
        SpawnV = 400
        SpawnP = 600
        SpeedC = 7
        SpeedC1 = int((SpeedC*100)/3)
        SpeedV = 7
        Track01="Textures\Tracks\Level2\Track22.png"
        SPMenu(Track01)
    def Level31():
        """
        Funcion la cual le da la velocidad a los velhiculos, el indice de aparicion de items y vehiculos y carga la imagen del Mapa
        """
        global MaxS,SpawnV,SpawnP,SpeedC,SpeedV,SpeedC1
        MaxS = 7
        SpawnV = 300
        SpawnP = 650
        SpeedC = 8
        SpeedC1 = int((SpeedC*100)/3)
        SpeedV = 7
        Track01="Textures\Tracks\Level3\Track32.png"
        SPMenu(Track01)
    def Level41():
        """
        Funcion la cual le da la velocidad a los velhiculos, el indice de aparicion de items y vehiculos y carga la imagen del Mapa
        """
        global MaxS,SpawnV,SpawnP,SpeedC,SpeedV,SpeedC1
        MaxS = 8
        SpawnV = 200
        SpawnP = 650
        SpeedC = 8
        SpeedC1 = int((SpeedC*100)/3)
        SpeedV = 8 
        Track01="Textures\Tracks\Level4\Track42.png"
        SPMenu(Track01)
    def Level51():
        """
        Funcion la cual le da la velocidad a los velhiculos, el indice de aparicion de items y vehiculos y carga la imagen del Mapa
        """
        global MaxS,SpawnV,SpawnP,SpeedC,SpeedV,SpeedC1
        MaxS = 10
        SpawnV = 150
        SpawnP = 700
        SpeedC = 9
        SpeedC1 = int((SpeedC*100)/3)
        SpeedV = 10
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

#========================================TWO PLAYERS=================================================#

def LvlsMenuV():
    """
    """
    def VersusMenu(Track02):
        """
        """
        def VersusGame():
            """
            Funcion principal para el modo un Versus
            """
            # Crea la ventana y la asocia a la variable v
            ventana3.destroy()
            v = Tk()
            v.resizable(width=False,height=False)
            v.geometry("1475x720+0+0")
            v.config(cursor="cross")
            v.title("Road Fighter")
            
            ImgTrack=PhotoImage(file=Track02)
            ImgTrack2=PhotoImage(file=Track02)
            ImgCar = PhotoImage(file="Textures/Vehicles/Runner/Runner2.png")
            ImgCar2 = PhotoImage(file="Textures/Vehicles/Minivan/Minivan2.png")
            ImgCar3 = PhotoImage(file="Textures/Vehicles/Fighter/Fighter2.png")
            filename = PhotoImage(file="Textures/Vehicles/User/User12.png")
            filename2 = PhotoImage(file="Textures/Vehicles/User/User2.png")

            ImgGas = PhotoImage(file="Textures/PowerUps/Gas2.png")
            ImgOil = PhotoImage(file="Textures/PowerUps/Oil2.png")
            ImgScore=PhotoImage(file="Textures/Menu/InGame.png")


            def BG():
                """
                Mueve la carretera dependiendo de la velocidad del nivel
                """
                global MaxS,MaxS2
                d.move(w,0,MaxS)
                d.move(w1,0,MaxS2)
                v.after(5,BG)

            def Fighter1(FighterX):
                q2 = d.create_image(FighterX,-87,image=ImgCar3)
                def MoverFighter1():
                    global SpeedV,gas1,score1,velocidady2,SpeedC1

                    posx1 = d.coords(x)[0]
                    posy1 = d.coords(x)[1]
                    posxx1 = d.coords(q2)[0]
                    posyy1 = d.coords(q2)[1]
                    
                    if(d.coords(q2)[1] <= 800):
                        
                        if(posx1 >= posxx1 and posx1 <= posxx1 + 25 and posy1 >= posyy1 and posy1 <= posyy1 + 80):
                            gas1 = gas1 - 10
                            score1 = score1 - 25
                            SpeedC1 = SpeedC1 -15
                            d.delete(q2)
                            return
                        if(posx1 <= posxx1 and posx1 + 25 >= posxx1 and posy1 <= posyy1 and posy1 + 80 <= posyy1):
                            gas1 = gas1 - 10
                            score1 = score1 - 25
                            SpeedC1 = SpeedC1 -15
                            d.delete(q2)
                            return
                        if(posx1 <= posxx1 and posx1 >= posxx1 - 25 and posy1 <= posyy1 and posy1 >= posyy1 - 80):
                            gas1 = gas1 - 10
                            score1 = score1 - 25
                            SpeedC1 = SpeedC1 -15
                            d.delete(q2)
                            return
                        if(posx1 >= posxx1 and posx1 + 25 <= posxx1 and posy1 >= posyy1 and posy1 + 80 >= posyy1):
                            gas1 = gas1 - 10
                            score1 = score1 - 25
                            SpeedC1 = SpeedC1 -15
                            d.delete(q2)
                            return

                        if(d.coords(q2)[0] > d.coords(x)[0]):
                            d.move(q2,-2,velocidady2)
                        if(d.coords(q2)[0] < d.coords(x)[0]):
                            d.move(q2,2,velocidady2)
                        if(d.coords(q2)[0] == d.coords(x)[0]):
                            d.move(q2,0,velocidady2)
                        
                    else:
                        d.delete(q2)
                        return

                        

                    v.after(10,MoverFighter1)
                MoverFighter1()

            def Fighter2(FighterX):
                q3 = d.create_image(FighterX+900,-87,image=ImgCar3)
                def MoverFighter2():
                    global SpeedV,gas2,score2,velocidady,SpeedC2

                    posx2 = d.coords(x1)[0]
                    posy2 = d.coords(x1)[1]
                    posxx2 = d.coords(q3)[0]
                    posyy2 = d.coords(q3)[1]

                    if(d.coords(q3)[1] <= 800):
                        if(posx2 >= posxx2 and posx2 <= posxx2 + 25 and posy2 >= posyy2 and posy2 <= posyy2 + 80):
                            gas2 = gas2 - 10
                            score2 = score2 - 25
                            SpeedC2 = SpeedC2 -15
                            d.delete(q3)
                            return
                        if(posx2 <= posxx2 and posx2 + 25 >= posxx2 and posy2 <= posyy2 and posy2 + 80 <= posyy2):
                            gas2 = gas2 - 10
                            score2 = score2 - 25
                            SpeedC2 = SpeedC2 -15
                            d.delete(q3)
                            return
                        if(posx2 <= posxx2 and posx2 >= posxx2 - 25 and posy2 <= posyy2 and posy2 >= posyy2 - 80):
                            gas2 = gas2 - 10
                            score2 = score2 - 25
                            SpeedC2 = SpeedC2 -15
                            d.delete(q3)
                            return
                        if(posx2 >= posxx2 and posx2 + 25 <= posxx2 and posy2 >= posyy2 and posy2 + 80 >= posyy2):
                            gas2 = gas2 - 10
                            score2 = score2 - 25
                            SpeedC2 = SpeedC2 -15
                            d.delete(q3)
                            return
                        
                        if(d.coords(q3)[0] > d.coords(x1)[0]):
                            d.move(q3,-2,velocidady2)
                        if(d.coords(q3)[0] < d.coords(x1)[0]):
                            d.move(q3,2,velocidady2)
                        if(d.coords(q3)[0] == d.coords(x1)[0]):
                            d.move(q3,0,velocidady2)

                    else:
                        d.delete(q3)
                        return
                    v.after(10,MoverFighter2)
                MoverFighter2()
                
            def Runner1(RunnerX):
                q1 = d.create_image(RunnerX,-87,image=ImgCar)
                def MoverRunner1():
                    global SpeedV,gas1,score1,velocidady2,velocidadx1
                    if(d.coords(q1)[1] <= 800 ):
                        
                        def MoveLeft1():
                            global SpeedV,gas1,score1,velocidady2,velocidadx1,SpeedC1
                            posx22 = d.coords(q1)[0]
                            posy22 = d.coords(q1)[1]
                            posx11 = d.coords(x)[0]
                            posy11 = d.coords(x)[1]
                            if(posx11 >= posx22 and posx11 <= posx22 + 25 and posy11 >= posy22 and posy11 <= posy22 + 80):
                                gas1 = gas1 - 10
                                score1 = score1 -20
                                SpeedC1 = SpeedC1 -15
                                d.delete(q1)
                                return
                            if(posx11 <= posx22 and posx11 + 25 >= posx22 and posy11 <= posy22 and posy11 + 80 <= posy22):
                                gas1 = gas1 - 10
                                score1 = score1 -20
                                SpeedC1 = SpeedC1 -15
                                d.delete(q1)
                                return
                            if(posx11 <= posx22 and posx11 >= posx22 - 25 and posy11 <= posy22 and posy11 >= posy22 - 80):
                                gas1 = gas1 - 10
                                score1 = score1 -20
                                SpeedC1 = SpeedC1 -15
                                d.delete(q1)
                                return
                            if(posx11 >= posx22 and posx11 + 25 <= posx22 and posy11 >= posy22 and posy11 + 80 >= posy22):
                                gas1 = gas1 - 10
                                score1 = score1 - 20
                                SpeedC1 = SpeedC1 -15
                                d.delete(q1)
                                return
                            
                            if(d.coords(q1)[0] > 170):
                                d.move(q1,-5,velocidady2)
                                v.after(10,MoveLeft1)
                            else:
                                MoveRight1()
                        def MoveRight1():
                            global SpeedV,gas1,score1,velocidady2,velocidadx1,SpeedC1
                            posx22 = d.coords(q1)[0]
                            posy22 = d.coords(q1)[1]
                            posx11 = d.coords(x1)[0]
                            posy11 = d.coords(x1)[1]
                            if(posx11 >= posx22 and posx11 <= posx22 + 25 and posy11 >= posy22 and posy11 <= posy22 + 80):
                                gas1 = gas1 - 10
                                score1 = score1 -20
                                SpeedC1 = SpeedC1 -15
                                d.delete(q1)
                                return
                            if(posx11 <= posx22 and posx11 + 25 >= posx22 and posy11 <= posy22 and posy11 + 80 <= posy22):
                                gas1 = gas1 - 10
                                score1 = score1 -20
                                SpeedC1 = SpeedC1 -15
                                d.delete(q1)
                                return
                            if(posx11 <= posx22 and posx11 >= posx22 - 25 and posy11 <= posy22 and posy11 >= posy22 - 80):
                                gas1 = gas1 - 10
                                score1 = score1 -20
                                SpeedC1 = SpeedC1 -15
                                d.delete(q1)
                                return
                            if(posx11 >= posx22 and posx11 + 25 <= posx22 and posy11 >= posy22 and posy11 + 80 >= posy22):
                                gas1 = gas1 - 10
                                score1 = score1 - 20
                                SpeedC1 = SpeedC1 -15
                                d.delete(q1)
                                return
                            
                            if(d.coords(q1)[0] < 450):
                                d.move(q1,5,velocidady2)
                                v.after(10,MoveRight1)
                            else:
                                MoveLeft1()
                        if(velocidadx1==1):
                            MoveRight1()
                        else:
                            MoveLeft1()
                    else:
                        d.delete(q1)
                        return
                            
                MoverRunner1()
                
            def Runner2(RunnerX):
                q2 = d.create_image(RunnerX+900,-87,image=ImgCar)
                def MoverRunner2():
                    global SpeedV,gas2,score2,velocidady2,velocidadx1
                    if(d.coords(q2)[1] <= 800 ):
                        
                        def MoveLeft2():
                            global SpeedV,gas2,score2,velocidady2,velocidadx1,SpeedC2
                            posx22 = d.coords(q2)[0]
                            posy22 = d.coords(q2)[1]
                            posx11 = d.coords(x)[0]
                            posy11 = d.coords(x)[1]
                            if(posx11 >= posx22 and posx11 <= posx22 + 25 and posy11 >= posy22 and posy11 <= posy22 + 80):
                                gas2 = gas2 - 10
                                score2 = score2 -20
                                SpeedC2 = SpeedC2 -15
                                d.delete(q2)
                                return
                            if(posx11 <= posx22 and posx11 + 25 >= posx22 and posy11 <= posy22 and posy11 + 80 <= posy22):
                                gas2 = gas2 - 10
                                score2 = score2 -20
                                SpeedC2 = SpeedC2 -15
                                d.delete(q2)
                                return
                            if(posx11 <= posx22 and posx11 >= posx22 - 25 and posy11 <= posy22 and posy11 >= posy22 - 80):
                                gas2 = gas2 - 10
                                score2 = score2 -20
                                SpeedC2 = SpeedC2 -15
                                d.delete(q2)
                                return
                            if(posx11 >= posx22 and posx11 + 25 <= posx22 and posy11 >= posy22 and posy11 + 80 >= posy22):
                                gas2 = gas2 - 10
                                score2 = score2 - 20
                                SpeedC2 = SpeedC2 -15
                                d.delete(q2)
                                return
                            
                            if(d.coords(q2)[0] > 1070):
                                d.move(q2,-5,velocidady2)
                                v.after(10,MoveLeft2)
                            else:
                                MoveRight2()
                        def MoveRight2():
                            global SpeedV,gas2,score2,velocidady2,velocidadx1,SpeedC2
                            posx22 = d.coords(q2)[0]
                            posy22 = d.coords(q2)[1]
                            posx11 = d.coords(x1)[0]
                            posy11 = d.coords(x1)[1]
                            if(posx11 >= posx22 and posx11 <= posx22 + 25 and posy11 >= posy22 and posy11 <= posy22 + 80):
                                gas2 = gas2 - 10
                                score2 = score2 -20
                                SpeedC2 = SpeedC2 -15
                                d.delete(q2)
                                return
                            if(posx11 <= posx22 and posx11 + 25 >= posx22 and posy11 <= posy22 and posy11 + 80 <= posy22):
                                gas2 = gas2 - 10
                                score2 = score2 -20
                                SpeedC2 = SpeedC2 -15
                                d.delete(q2)
                                return
                            if(posx11 <= posx22 and posx11 >= posx22 - 25 and posy11 <= posy22 and posy11 >= posy22 - 80):
                                gas2 = gas2 - 10
                                score2 = score2 -20
                                SpeedC2 = SpeedC2 -15
                                d.delete(q2)
                                return
                            if(posx11 >= posx22 and posx11 + 25 <= posx22 and posy11 >= posy22 and posy11 + 80 >= posy22):
                                gas2 = gas2 - 10
                                score2 = score2 - 20
                                SpeedC2 = SpeedC2 -15
                                d.delete(q2)
                                return
                            
                            if(d.coords(q2)[0] < 1350):
                                d.move(q2,5,velocidady2)
                                v.after(10,MoveRight2)
                            else:
                                MoveLeft2()
                        if(velocidadx1==1):
                            MoveRight2()
                        else:
                            MoveLeft2()
                    else:
                        d.delete(q2)
                        return
                            
                MoverRunner2()


            def Minivan1(MinivanX):
                q1 = d.create_image(MinivanX,-87,image=ImgCar2)
                
                def MoverMinivan1():
                    global SpeedV,score1,gas1,velocidady2,SpeedC1

                    posx1 = d.coords(x)[0]
                    posy1 = d.coords(x)[1]
                    posxx1 = d.coords(q1)[0]
                    posyy1 = d.coords(q1)[1]
                    
                    if(d.coords(q1)[1] <= 10000 ):
                        d.move(q1,0,velocidady2)
                        if(posx1 >= posxx1 and posx1 <= posxx1 + 25 and posy1 >= posyy1 and posy1 <= posyy1 + 80):
                            gas1 = gas1 - 10
                            score1 = score1 -25
                            SpeedC1 = SpeedC1 -15
                            d.delete(q1)
                            return
                        if(posx1 <= posxx1 and posx1 + 25 >= posxx1 and posy1 <= posyy1 and posy1 + 80 <= posyy1):
                            gas1 = gas1 - 10
                            score1 = score1 -25
                            SpeedC1 = SpeedC1 -15
                            d.delete(q1)
                            return
                        if(posx1 <= posxx1 and posx1 >= posxx1 - 25 and posy1 <= posyy1 and posy1 >= posyy1 - 80):
                            gas1 = gas1 - 10
                            score1 = score1 -25
                            SpeedC1 = SpeedC1 -15
                            d.delete(q1)
                            return
                        if(posx1 >= posxx1 and posx1 + 25 <= posxx1 and posy1 >= posyy1 and posy1 + 80 >= posyy1):
                            gas1 = gas1 - 10
                            score1 = score1 -25
                            SpeedC1 = SpeedC1 -15
                            d.delete(q1)
                            return
                    else:
                        d.delete(q1)
                        return
                    
                    
                    
                    v.after(10,MoverMinivan1)
                MoverMinivan1()
                
            def Minivan2(MinivanX):
                q2 = d.create_image(MinivanX+900,-87,image=ImgCar2)
                def MoverMinivan2():
                    global SpeedV,score2,gas2,velocidady2,SpeedC2

                    posx2 = d.coords(x1)[0]
                    posy2 = d.coords(x1)[1]
                    posxx2 = d.coords(q2)[0]
                    posyy2 = d.coords(q2)[1]

                    if(d.coords(q2)[1] <= 10000 ):
                        d.move(q2,0,velocidady2)
                        if(posx2 >= posxx2 and posx2 <= posxx2 + 25 and posy2 >= posyy2 and posy2 <= posyy2 + 80):
                            gas2 = gas2 - 10
                            score2 = score2 -25
                            SpeedC2 = SpeedC2 -15
                            d.delete(q2)
                            return
                        if(posx2 <= posxx2 and posx2 + 25 >= posxx2 and posy2 <= posyy2 and posy2 + 80 <= posyy2):
                            gas2 = gas2 - 10
                            score2 = score2 -25
                            SpeedC2 = SpeedC2 -15
                            d.delete(q2)
                            return
                        if(posx2 <= posxx2 and posx2 >= posxx2 - 25 and posy2 <= posyy2 and posy2 >= posyy2 - 80):
                            gas2 = gas2 - 10
                            score2 = score2 -25
                            SpeedC2 = SpeedC2 -15
                            d.delete(q2)
                            return
                        if(posx2 >= posxx2 and posx2 + 25 <= posxx2 and posy2 >= posyy2 and posy2 + 80 >= posyy2):
                            gas2 = gas2 - 10
                            score2 = score2 -25
                            SpeedC2 = SpeedC2 -15
                            d.delete(q2)
                            return
                    else:
                        d.delete(q2)
                        return
                    v.after(10,MoverMinivan2)
                MoverMinivan2()

            def PowerGas1(GasX):
                q1 = d.create_image(GasX,-87,image=ImgGas)
                def MoveGas1():
                    global gas1,MaxS,score1
                    posx22 = d.coords(q1)[0]
                    posy22 = d.coords(q1)[1]
                    posx11 = d.coords(x)[0]
                    posy11 = d.coords(x)[1]
                    
                    if(d.coords(q1)[1] <= 800 ):
                        d.move(q1,0,7)
                        if(posx11 >= posx22 and posx11 <= posx22 + 25 and posy11 >= posy22 and posy11 <= posy22 + 80):
                            gas1 = gas1 + 20
                            score1 = score1 + 15
                            d.delete(q1)
                            return
                        if(posx11 <= posx22 and posx11 + 25 >= posx22 and posy11 <= posy22 and posy11 + 80 <= posy22):
                            gas1 = gas1 + 20
                            score1 = score1 + 15
                            d.delete(q1)
                            return
                        if(posx11 <= posx22 and posx11 >= posx22 - 25 and posy11 <= posy22 and posy11 >= posy22 - 80):
                            gas1 = gas1 + 20
                            score1 = score1 + 15
                            d.delete(q1)
                            return
                        if(posx11 >= posx22 and posx11 + 25 <= posx22 and posy11 >= posy22 and posy11 + 80 >= posy22):
                            gas1 = gas1 + 20
                            score1 = score1 + 15
                            d.delete(q1)
                            return
                    
                    else:
                        d.delete(q1)
                        return
                    
                    if(MaxS != 0):
                        v.after(10,MoveGas1)
                MoveGas1()

            def PowerGas2(GasX):
                q2 = d.create_image(GasX+900,-87,image=ImgGas)
                def MoveGas2():
                    global gas2,MaxS,score2
                    posx22 = d.coords(q2)[0]
                    posy22 = d.coords(q2)[1]
                    posx11 = d.coords(x1)[0]
                    posy11 = d.coords(x1)[1]
                    
                    if(d.coords(q2)[1] <= 800 ):
                        d.move(q2,0,7)
                        if(posx11 >= posx22 and posx11 <= posx22 + 25 and posy11 >= posy22 and posy11 <= posy22 + 80):
                            gas2 = gas2 + 20
                            score2 = score2 + 15
                            d.delete(q2)
                            return
                        if(posx11 <= posx22 and posx11 + 25 >= posx22 and posy11 <= posy22 and posy11 + 80 <= posy22):
                            gas2 = gas2 + 20
                            score2 = score2 + 15
                            d.delete(q2)
                            return
                        if(posx11 <= posx22 and posx11 >= posx22 - 25 and posy11 <= posy22 and posy11 >= posy22 - 80):
                            gas2 = gas2 + 20
                            score2 = score2 + 15
                            d.delete(q2)
                            return
                        if(posx11 >= posx22 and posx11 + 25 <= posx22 and posy11 >= posy22 and posy11 + 80 >= posy22):
                            gas2 = gas2 + 20
                            score2 = score2 + 15
                            d.delete(q2)
                            return
                    
                    else:
                        d.delete(q2)
                        return
                    
                    if(MaxS != 0):
                        v.after(10,MoveGas2)
                MoveGas2()

            def Oil1(OilX):
                q1 = d.create_image(OilX,-87,image=ImgOil)
                def MoveOil1():
                    global MaxS,SpeedC1
                    posx22 = d.coords(q1)[0]
                    posy22 = d.coords(q1)[1]
                    posx11 = d.coords(x)[0]
                    posy11 = d.coords(x)[1]

                    if(d.coords(q1)[1] <= 800 ):
                        d.move(q1,0,MaxS)

                        if(posx22 <= 310):
                            if(posx11 >= posx22 and posx11 <= posx22 + 25 and posy11 >= posy22 and posy11 <= posy22 + 80):
                                d.move(x,10,0)
                                SpeedC1 = SpeedC1 -5
                            if(posx11 <= posx22 and posx11 + 25 >= posx22 and posy11 <= posy22 and posy11 + 80 <= posy22):
                                d.move(x,10,0)
                                SpeedC1 = SpeedC1 -5
                            if(posx11 <= posx22 and posx11 >= posx22 - 25 and posy11 <= posy22 and posy11 >= posy22 - 80):
                                d.move(x,10,0)
                                SpeedC1 = SpeedC1 -5
                            if(posx11 >= posx22 and posx11 + 25 <= posx22 and posy11 >= posy22 and posy11 + 80 >= posy22):
                                d.move(x,10,0)
                                SpeedC1 = SpeedC1 -5
                        if(posx22 > 310):
                            if(posx11 >= posx22 and posx11 <= posx22 + 25 and posy11 >= posy22 and posy11 <= posy22 + 80):
                                d.move(x,-10,0)
                                SpeedC1 = SpeedC1 -5
                            if(posx11 <= posx22 and posx11 + 25 >= posx22 and posy11 <= posy22 and posy11 + 80 <= posy22):
                                d.move(x,-10,0)
                                SpeedC1 = SpeedC1 -5
                            if(posx11 <= posx22 and posx11 >= posx22 - 25 and posy11 <= posy22 and posy11 >= posy22 - 80):
                                d.move(x,-10,0)
                                SpeedC1 = SpeedC1 -5
                            if(posx11 >= posx22 and posx11 + 25 <= posx22 and posy11 >= posy22 and posy11 + 80 >= posy22):
                                d.move(x,-10,0)
                                SpeedC1 = SpeedC1 -5
                    
                    else:
                        d.delete(q1)
                        return
                    if(MaxS != 0):
                        v.after(10,MoveOil1)
                MoveOil1()

            def Oil2(OilX):
                q1 = d.create_image(OilX+900,-87,image=ImgOil)
                def MoveOil2():
                    global MaxS,SpeedC2
                    posx22 = d.coords(q1)[0]
                    posy22 = d.coords(q1)[1]
                    posx11 = d.coords(x1)[0]
                    posy11 = d.coords(x1)[1]

                    if(d.coords(q1)[1] <= 800 ):
                        d.move(q1,0,MaxS)

                        if(posx22 <= 1210):
                            if(posx11 >= posx22 and posx11 <= posx22 + 25 and posy11 >= posy22 and posy11 <= posy22 + 80):
                                d.move(x1,10,0)
                                SpeedC2 = SpeedC2 -5
                            if(posx11 <= posx22 and posx11 + 25 >= posx22 and posy11 <= posy22 and posy11 + 80 <= posy22):
                                d.move(x1,10,0)
                                SpeedC2 = SpeedC2 -5
                            if(posx11 <= posx22 and posx11 >= posx22 - 25 and posy11 <= posy22 and posy11 >= posy22 - 80):
                                d.move(x1,10,0)
                                SpeedC2 = SpeedC2 -5
                            if(posx11 >= posx22 and posx11 + 25 <= posx22 and posy11 >= posy22 and posy11 + 80 >= posy22):
                                d.move(x1,10,0)
                                SpeedC2 = SpeedC2 -5
                        if(posx22 > 1210):
                            if(posx11 >= posx22 and posx11 <= posx22 + 25 and posy11 >= posy22 and posy11 <= posy22 + 80):
                                d.move(x1,-10,0)
                                SpeedC2 = SpeedC2 -5
                            if(posx11 <= posx22 and posx11 + 25 >= posx22 and posy11 <= posy22 and posy11 + 80 <= posy22):
                                d.move(x1,-10,0)
                                SpeedC2 = SpeedC2 -5
                            if(posx11 <= posx22 and posx11 >= posx22 - 25 and posy11 <= posy22 and posy11 >= posy22 - 80):
                                d.move(x1,-10,0)
                                SpeedC2 = SpeedC2 -5
                            if(posx11 >= posx22 and posx11 + 25 <= posx22 and posy11 >= posy22 and posy11 + 80 >= posy22):
                                d.move(x1,-10,0)
                                SpeedC2 = SpeedC2 -5
                    
                    else:
                        d.delete(q1)
                        return
                    if(MaxS != 0):
                        v.after(10,MoveOil2)
                MoveOil2()
            
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
                global h,SpeedV
                if(MaxS != 0):
                    if(68 in h):
                        if(d.coords(x)[0] < 450):
                            d.move(x,SpeedV,0)
                    if(65 in h):
                        if(d.coords(x)[0] > 170):
                            d.move(x,-(SpeedV),0)
                if(MaxS2 != 0):
                    if(74 in h):
                        if(d.coords(x1)[0] > 1070):
                            d.move(x1,-(SpeedV),0)
                    if(76 in h):
                        if(d.coords(x1)[0] < 1350):
                            d.move(x1,SpeedV,0)
                d.after(15,key)
                


            def Gas():
                global gas1,gas2,MaxS,MaxS2,Player1W,Player2W,score1,score2
                LblGas1 = Label(d,text = str(gas1),bg="black",fg="white",font =("8bitoperator JVE",40)).place(x=650,y=400)
                LblGas2 = Label(d,text = str(gas2),bg="black",fg="white",font =("8bitoperator JVE",40)).place(x=800,y=400)
                d.delete(LblGas1)
                d.delete(LblGas2)
                if(gas1>0):
                    gas1 = gas1 - 1
                if(gas2>0):
                    gas2 = gas2 - 1
                if(gas1<=0):
                    gas1 = 0
                    MaxS = 0
                    d.delete(LblGas1)
                    LblGas1 = Label(d,text = str(gas1),bg="black",fg="white",font =("8bitoperator JVE",40)).place(x=650,y=400)
                    LblOutGas = Label(d,text = "OUT OF GAS :(", bg="black",fg="white",font =("8bitoperator JVE",50)).place(x=100,y=300)
                    Player1W = False
                if(gas2<=0):
                    gas2 = 0
                    MaxS2 = 0
                    d.delete(LblGas2)
                    LblGas2 = Label(d,text = str(gas2),bg="black",fg="white",font =("8bitoperator JVE",40)).place(x=650,y=400)
                    LblOutGas = Label(d,text = "OUT OF GAS :(", bg="black",fg="white",font =("8bitoperator JVE",50)).place(x=1000,y=300)
                    Player2W = False

                if(Player1W == False and Player2W == False):
                    if(score1 > score2):
                        LblWinner = Label(d,text = "Winner: "+ Player12.get(),bg="white",fg="black",font =("8bitoperator JVE",100)).place(x=320,y=300)
                        d.after(2000,exit)
                    if(score2 > score2):
                        LblWinner = Label(d,text = "Winner: "+ Player22.get(),bg="white",fg="black",font =("8bitoperator JVE",100)).place(x=320,y=300)
                        d.after(2000,exit)
                    if(score1 == score2):
                        LblWinner = Label(d,text = "DRAW",bg="white",fg="black",font =("8bitoperator JVE",100)).place(x=600,y=300)
                        d.after(2000,exit)
                    

                d.after(500,Gas)
            

            def Speed():
                """
                Funcion la cual muestra en un label la velocidad a la que va el usuario
                """
                global SpeedC,SpeedC1,SpeedC2,MaxS
                if(MaxS !=0):
                    if(Track02 == "Textures\Tracks\Level5\Track522.png"):
                        LblSpeed1 = Label(d,text = "Speed: 999",bg="black",fg="white",font=("8bitoperator JVE",40)).place(x=640,y=200)
                    else:
                        if(SpeedC1 < int((SpeedC*100)/3)):
                            SpeedC1 = SpeedC1 + 1
                        LblSpeed1 = Label(d,text = "Speed: " + str(SpeedC1) ,bg="black",fg="white",font=("8bitoperator JVE",40)).place(x=640,y=200)
                        d.delete(LblSpeed1)
                else:
                    LblSpeed1 = Label(d,text = "Speed: 000",bg="black",fg="white",font=("8bitoperator JVE",40)).place(x=640,y=200)
                if(MaxS2 !=0):
                    if(Track02 == "Textures\Tracks\Level5\Track522.png"):
                        LblSpeed2 = Label(d,text = "Speed: 999",bg="black",fg="white",font=("8bitoperator JVE",40)).place(x=640,y=260)
                    else:
                        if(SpeedC2 < int((SpeedC*100)/3)):
                            SpeedC2 = SpeedC2 + 1
                        LblSpeed2 = Label(d,text = "Speed: " + str(SpeedC2) ,bg="black",fg="white",font=("8bitoperator JVE",40)).place(x=640,y=260)
                        d.delete(LblSpeed2)
                else:
                    LblSpeed2 = Label(d,text = "Speed: 000",bg="black",fg="white",font=("8bitoperator JVE",40)).place(x=640,y=260)
                d.after(200,Speed)
            
            def Score():
                global score1,score2,Player1W,Player2W
                if(Player1W == True):
                    score1 = score1 + 15
                if(Player2W == True):
                    score2 = score2 + 15
                
                LblScore1 = Label(v,text = str(score1),bg="black",fg="white",font =("8bitoperator JVE",40)).place(x=650,y=585)
                LblScore2 = Label(v,text = str(score2),bg="black",fg="white",font =("8bitoperator JVE",40)).place(x=750,y=540)
                d.after(100,Score)
            # Crea los widgets
            d = Canvas(v, width=1475, height=720, )





            w = d.create_image(300,-8800,image=ImgTrack)
            w1= d.create_image(1200,-8800,image=ImgTrack)

            d.bind("<KeyPress>",keydown)
            d.bind("<KeyRelease>",keyup)

            d.focus_set()

            
            d.pack()

            
            x = d.create_image(310,620,image=filename)
            x1= d.create_image(1210,620,image=filename2)


            def Random2():
                global SpeedV,velocidady2,SpawnV,SpawnP
                RandomV = random.randint(0,SpawnV)
                if(RandomV == 0):
                    MinivanX = random.randint(170,450)
                    velocidady2 = random.randint(4,SpeedV)
                    Minivan1(MinivanX)
                    Minivan2(MinivanX)
                if(RandomV == 1):
                    RunnerX = random.randint(170,450)
                    velocidady2 = random.randint(4,SpeedV)
                    velocidadx1 = random.randint(0,1)
                    Runner1(RunnerX)
                    Runner2(RunnerX)
                if(RandomV == 2):
                    FighterX = random.randint(170,450)
                    velocidady2 = random.randint(2,SpeedV)
                    Fighter1(FighterX)
                    Fighter2(FighterX)
                RandomG = random.randint(0,SpawnP)
                if(RandomG == 250 and MaxS !=0):
                    GasX = random.randint(170,450)
                    PowerGas1(GasX)
                    PowerGas2(GasX)
                if(RandomG == 150 and MaxS !=0):
                    OilX = random.randint(170,450)
                    Oil1(OilX)
                    Oil2(OilX)
                v.after(10,Random2)

            #==========Se cargan Todos los elementos============#
            BG()
            key()
            Random2()
            Gas()
            Speed()
            Score()
            #===================================================#
            d.create_image(-375,0,image=ImgScore,anchor=NW)

            LblPlayer12 = Label(v,text = Player12.get(),bg="black",fg="white",font =("8bitoperator JVE",35)).place(x=630,y=70)
            LblPlayer22 = Label(v,text = Player22.get(),bg="black",fg="white",font =("8bitoperator JVE",35)).place(x=710,y=120)
            
    
            v.mainloop()
        
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
        btnSPMenu=Button(ventana3,width=150,height=75,image=imgBtnSPmenu,command=VersusGame).place(x=575,y=420)

        Player12 = StringVar()
        Player22 = StringVar()
        Player12.set("Player 1")
        Player22.set("Player 2")
        #### Text Box ####
        txtPlayer1=Entry(ventana3,font=("8bitoperator JVE",40),textvariable = Player12,width=20).place(x=600,y=160)
        txtPlayer2=Entry(ventana3,font=("8bitoperator JVE",40),textvariable = Player22,width=20).place(x=600,y=300)

        ventana3.mainloop()

    def Level12():
        """
        Funcion la cual le da la velocidad a los velhiculos, el indice de aparicion de items y vehiculos y carga la imagen del Mapa
        """
        global MaxS,MaxS2,SpawnV,SpawnP,SpeedC,SpeedV,SpeedC1,SpeedC2
        MaxS = 4
        MaxS2 = 4
        SpawnV = 500
        SpawnP = 600
        SpeedC = 7
        SpeedC1 = int((SpeedC*100)/3)
        SpeedC2 = int((SpeedC*100)/3)
        SpeedV = 7
        Track02 = "Textures\Tracks\Level1\Track122.png"
        VersusMenu(Track02)
    def Level22():
        """
        Funcion la cual le da la velocidad a los velhiculos, el indice de aparicion de items y vehiculos y carga la imagen del Mapa
        """
        global MaxS,MaxS2,SpawnV,SpawnP,SpeedC,SpeedV,SpeedC1,SpeedC2
        MaxS = 6
        MaxS2 = 6
        SpawnV = 400
        SpawnP = 600
        SpeedC = 7
        SpeedC1 = int((SpeedC*100)/3)
        SpeedC2 = int((SpeedC*100)/3)
        SpeedV = 7
        Track02 = "Textures\Tracks\Level2\Track222.png"
        VersusMenu(Track02)
    def Level32():
        """
        Funcion la cual le da la velocidad a los velhiculos, el indice de aparicion de items y vehiculos y carga la imagen del Mapa
        """
        global MaxS,MaxS2,SpawnV,SpawnP,SpeedC,SpeedV,SpeedC1,SpeedC2
        MaxS = 7
        MaxS2 = 7
        SpawnV = 300
        SpawnP = 650
        SpeedC = 8
        SpeedC1 = int((SpeedC*100)/3)
        SpeedC2 = int((SpeedC*100)/3)
        SpeedV = 7
        Track02 = "Textures\Tracks\Level3\Track322.png"
        VersusMenu(Track02)
    def Level42():
        """
        Funcion la cual le da la velocidad a los velhiculos, el indice de aparicion de items y vehiculos y carga la imagen del Mapa
        """
        global MaxS,MaxS2,SpawnV,SpawnP,SpeedC,SpeedV,SpeedC1,SpeedC2
        MaxS = 8
        MaxS2 = 8
        SpawnV = 200
        SpawnP = 650
        SpeedC = 8
        SpeedC1 = int((SpeedC*100)/3)
        SpeedC2 = int((SpeedC*100)/3)
        SpeedV = 8
        Track02 = "Textures\Tracks\Level4\Track422.png"
        VersusMenu(Track02)
    def Level52():
        """
        Funcion la cual le da la velocidad a los velhiculos, el indice de aparicion de items y vehiculos y carga la imagen del Mapa
        """
        global MaxS,MaxS2,SpawnV,SpawnP,SpeedC,SpeedV,SpeedC1,SpeedC2
        MaxS = 10
        MaxS2 = 10
        SpawnV = 150
        SpawnP = 700
        SpeedC = 9
        SpeedV = 10
        Track02 = "Textures\Tracks\Level5\Track522.png"
        VersusMenu(Track02)
        
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
    Funcion que cierra la ventana principal y cierra el proceso
    """
    ventana1.destroy()
    exit()

#==================================================================================================#
def Instructions():
    """
    Funcion la cual genera un menu en donde se encuentran las instrucciones del usuario
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
