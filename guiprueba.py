from random import choice
from tkinter import *
from PIL import ImageTk, Image

def show_frame(frame):
    frame.tkraise()

window = Tk()
rockImg = ImageTk.PhotoImage(Image.open(r'../PiedraPapeloTijeras/img/rock.png').resize((100,100)))
paperImg = ImageTk.PhotoImage(Image.open(r'../PiedraPapeloTijeras/img/paper.png').resize((100,100)))
scissorsImg = ImageTk.PhotoImage(Image.open(r'../PiedraPapeloTijeras/img/scissors.png').resize((100,100)))
window.state('zoomed')
window.title("Piedra, papel o tijeras en Python!")

window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)

menu = Frame(window) #menu
juego = Frame(window) #juego

for frame in (menu, juego):
    frame.grid(row=0,column=0,sticky="nsew")

#Menu
show_frame(menu)

def getGamertag():
    user = gamertag.get()
    show_frame(juego)
    return user

label = Label(menu, text = "Ingrese un nombre de usuario") 
label.pack()

gamertag = Entry(menu)
gamertag.pack()

saveGamertag = Button(menu, text="Guardar",command=getGamertag)
saveGamertag.pack()

#Juego
def play(opt):
    options = ['Piedra', 'Papel', 'Tijeras']
    playerOpt = (opt)
    CPUOpt = (choice(options))

    labelCPUOpt["text"] = "CPU select " + CPUOpt
    labelPlayerOpt["text"] = getGamertag() + " select " + playerOpt

    if(playerOpt == CPUOpt):
        result = "Empate" 
        color = "black"
    if((playerOpt == "Piedra" and CPUOpt=="Papel") or (playerOpt == "Papel" and CPUOpt=="Tijeras") or (playerOpt=="Tijeras" and CPUOpt=="Piedra")):
        result = "Perdiste"
        color = "red"  
    if((playerOpt == "Piedra" and CPUOpt=="Tijeras") or (playerOpt == "Papel" and CPUOpt=="Piedra") or (playerOpt=="Tijeras" and CPUOpt=="Papel")):
        result = "Ganaste"
        color = "green"
    
    labelResult["text"] = result
    labelResult["foreground"] = color

rock = Button(juego,image = rockImg,padx= 40, pady= 20, command=lambda: play("Piedra"))
rock.grid(row=1,column=0, padx=(600,0))
paper = Button(juego, image = paperImg, padx= 40, pady= 20, command=lambda: play("Papel"))
paper.grid(row=1,column=1)
scissors = Button(juego, image = scissorsImg, padx= 40, pady= 20, command=lambda: play("Tijeras"))
scissors.grid(row=1,column=2)

labelPlayerOpt = Label(juego)
labelPlayerOpt.grid(row=2,column=1)

labelCPUOpt = Label(juego)
labelCPUOpt.grid(row=3,column=1)

labelResult = Label(juego)
labelResult.grid(row=4,column=1)

exitButton = Button(juego, text="Salir",command=lambda: show_frame(menu))
exitButton.grid(row=5,column=1)

window.mainloop()