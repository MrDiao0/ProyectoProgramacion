from tkinter import *

def LvlsMenuS():
    """
    """
    def SPMenu():
        """
        """
        ventana2.destroy()
        
        ventana3=Tk()
        ventana3.geometry("1280x720+0+0")
        ventana3.config(cursor="cross")
        ventana3.title("Road Fighter")

        Fondo=PhotoImage(file="Textures\Menu\SinglePlayer Menu\SinglePlayerName.png")
        label01=Label(ventana3,image=Fondo).place(x=0,y=0)

        #### Buttons ####
        imgBtnSPmenu=PhotoImage(file="Textures\Menu\SinglePlayer Menu\Play.png")
        btnSPMenu=Button(ventana3,width=150,height=75,image=imgBtnSPmenu).place(x=575,y=350)

        #### Text Box ####
        txtPlayer1=Entry(ventana3,font=("Arial",40),width=20).place(x=620,y=180)

        ventana3.mainloop()
    def Level11():
        """
        """
        ImgTrack=PhotoImage(file="Textures\Tracks\Level1\Track1.png")
        SPMenu()
    def Level21():
        """
        """
        ImgTrack=PhotoImage(file="Textures\Tracks\Level2\Track2.png")
        SPMenu()
    def Level31():
        """
        """
        ImgTrack=PhotoImage(file="Textures\Tracks\Level3\Track3.png")
        SPMenu()
    def Level41():
        """
        """
        ImgTrack=PhotoImage(file="Textures\Tracks\Level4\Track4.png")
        SPMenu()
    def Level51():
        """
        """
        ImgTrack=PhotoImage(file="Textures\Tracks\Level5\Track5.png")
        SPMenu()
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
    
#### Start Menu #####
ventana1=Tk()
ventana1.geometry("1280x720+0+0")
ventana1.config(cursor="cross")
ventana1.title("Road Fighter")

imagen=PhotoImage(file="Textures\Menu\Start Menu\StartMenu.png")
lblimg=Label(ventana1,image=imagen).place(x=0,y=0)

#### Buttons Start Menu ####
imgBtnSP=PhotoImage(file="Textures\Menu\Start Menu\Buttons\SinglePlayer.png")
btnSP=Button(ventana1,width=150,height=75,image=imgBtnSP,command=LvlsMenuS).place(x=575,y=300)

imgBtnVersus=PhotoImage(file="Textures\Menu\Start Menu\Buttons\Versus.png")
btnVersus=Button(ventana1,width=150,
                 height=75,image=imgBtnVersus,command=LvlsMenuV).place(x=575,y=400)

imgBtnExit=PhotoImage(file="Textures\Menu\Start Menu\Buttons\Exit.png")
btnExit=Button(ventana1,width=150,height=75,image=imgBtnExit,command=Exit).place(x=575,y=500)

ventana1.mainloop()

#==================================================================================================#
