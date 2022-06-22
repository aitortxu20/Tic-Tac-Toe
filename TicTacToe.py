from tkinter import *
import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import simpledialog
import time

# Window Config

window = Tk()
window.title('Tic Tac Toe')
window.geometry('375x375')
window.configure(bg = 'green')


namePlayer1 = simpledialog.askstring('Player ', 'Write the name of player 1: ')
namePlayer2 = simpledialog.askstring('Player', 'Write the name of player 2:')
t = []
count = 0

for i in range(0,9):
    t.append('N')

turno = 0
buttonsList = []

# User Config

def start():
    window.destroy()
    window2 = Tk()
    window2.geometry('300x300')
    window2.configure(bg='black')

    def change(num):
        global turno,namePlayer1, namePlayer2, count
        if t[num] == 'N' and turno == 0:
            buttonsList[num].config(text = 'X')
            t[num] = 'X'
            turno = 1
            playerTurn.set('Turno : ' + namePlayer2)
        elif t[num] == 'N' and turno == 1:
            buttonsList[num].config(text='O')
            t[num] = 'O'
            turno = 0
            playerTurn.set('Turno : ' + namePlayer1)
        buttonsList[num].config(state = 'disable') and turno
        ganador()

    boton1 = Button(window2, width=5, height=2, bg='white', command = lambda : change(0))
    buttonsList.append(boton1)
    boton2 = Button(window2, width=5, height=2, bg='white', command = lambda : change(1))
    buttonsList.append(boton2)
    boton3 = Button(window2, width=5, height=2, bg='white', command = lambda : change(2))
    buttonsList.append(boton3)
    boton4 = Button(window2, width=5, height=2, bg='white', command = lambda : change(3))
    buttonsList.append(boton4)
    boton5 = Button(window2, width=5, height=2, bg='white', command = lambda : change(4))
    buttonsList.append(boton5)
    boton6 = Button(window2, width=5, height=2, bg='white', command = lambda : change(5))
    buttonsList.append(boton6)
    boton7 = Button(window2, width=5, height=2, bg='white', command = lambda : change(6))
    buttonsList.append(boton7)
    boton8 = Button(window2, width=5, height=2, bg='white', command = lambda : change(7))
    buttonsList.append(boton8)
    boton9 = Button(window2, width=5, height=2, bg='white', command = lambda : change(8))
    buttonsList.append(boton9)

    boton1.grid(row=0, column=0, padx=10, pady=10)
    boton2.grid(row=0, column=1, padx=10, pady=10)
    boton3.grid(row=0, column=2, padx=10, pady=10)
    boton4.grid(row=1, column=0, padx=10, pady=10)
    boton5.grid(row=1, column=1, padx=10, pady=10)
    boton6.grid(row=1, column=2, padx=10, pady=10)
    boton7.grid(row=2, column=0, padx=10, pady=10)
    boton8.grid(row=2, column=1, padx=10, pady=10)
    boton9.grid(row=2, column=2, padx=10, pady=10)

    # Turns

    playerTurn = StringVar()
    playerTurn.set('Turn : ' + namePlayer1)
    turno = Label(window2, textvariable = playerTurn).place(x = 210, y = 10)
    # turno2 = namePlayer2m

    window2.mainloop()



def ganador():

    # Winner in a horizontal way

    if (t[0] == 'X' and t[1] == 'X' and t[2] == 'X') or (t[3] == 'X' and t[4] == 'X' and t[5] == 'X') or (t[6] == 'X' and t[7] == 'X' and t[8] == 'X'):
        messagebox.showinfo('Winner', "You win: " + namePlayer1)
    elif (t[0] == 'O' and t[1] == 'O' and t[2] == 'O') or (t[3] == 'O' and t[4] == 'O' and t[5] == 'O') or (t[6] == 'O' and t[7] == 'O' and t[8] == 'O'):
        messagebox.showinfo('Winner', "You win: " + namePlayer2)
    elif (t[0] == 'X' and t[3] == 'X' and t[6] == 'X') or (t[1] == 'X' and t[4] == 'X' and t[7] == 'X') or (t[2] == 'X' and t[5] == 'X' and t[8] == 'X'):
        messagebox.showinfo('Winner', "You win: " + namePlayer1)

    # Winner in a vertical way

    elif (t[0] == 'O' and t[3] == 'O' and t[6] == 'O') or (t[1] == 'O' and t[4] == 'O' and t[7] == 'O') or (t[2] == 'O' and t[5] == 'O' and t[8] == 'O'):
        messagebox.showinfo('Winner', "You win: " + namePlayer2)
    elif (t[0] == 'X' and t[4] == 'X' and t[8] == 'X') or (t[2] == 'X' and t[4] == 'X' and t[6] == 'X'):
        messagebox.showinfo('Winner', "You win: " + namePlayer1)

    # Winner in a diagonal way

    elif (t[0] == 'O' and t[4] == 'O' and t[8] == 'O') or (t[2] == 'O' and t[4] == 'O' and t[6] == 'O'):
        messagebox.showinfo('Winner', "You win: " + namePlayer2)

#Buttons

botonstartuser = Button(window, text = 'Start!!!', width = 33, height = 2, bg = 'red', command = lambda : start())
botonstartuser.grid(row = 2, column = 2,columnspan = 2, pady = 140, padx = 72)


window.mainloop()