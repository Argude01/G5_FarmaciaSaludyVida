from tkinter import *
import os
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
import sqlite3
import os
import time


def insertar():
    raiz.destroy()
    import Leer_insertar



raiz=Tk()
raiz.title("INICIO")
raiz.resizable(1,1)
raiz.geometry("700x600")
raiz.config(bg="RoyalBlue",)
raiz.resizable(0,0)
img = ImageTk.PhotoImage(Image.open("SALUD.png"))

imglabel = Label(raiz, image=img).place(x=235,y=199)

Label(raiz, text="FARMACIA SALUD Y VIDA", fon=15, bg="Gold").place(x=250,y=10)

Label(raiz, text="12 BTP Seccion A ", fon=10, bg="Gold",fg="black").place(x=280,y=50)
Label(raiz, text="NUESTRO PROYECTO FUE HECHO CON LA FINALIDAD    ", fon=4, bg="Gold",fg="black").place(x=145,y=89)
Label(raiz, text="DE QUE NUESTROS CLIENTES TENGA BIENESTAR Y FACILIDAD DE MEDICAMENTOS ", fon=10, bg="Gold",fg="black").place(x=20,y=115)
Label(raiz, text="PARA SATISFACER LAS NECESIDADES DEL CLIENTE", fon=10, bg="Gold",fg="black").place(x=147,y=145)

Label(raiz, text="02 Annette Suazo", fon=6, bg="Gold",fg="black").place(x=40,y=230)
Label(raiz, text="09 Keydi Velasquez", fon=6, bg="Gold",fg="black").place(x=40,y=280)
Label(raiz, text="22 Stephanie Acosta", fon=6, bg="Gold",fg="black").place(x=40,y=340)
Label(raiz, text="23 Waleska Martinez", fon=6, bg="Gold",fg="black").place(x=490,y=230)
Label(raiz, text="25 Yeiri Maldonado", fon=6, bg="Gold",fg="black").place(x=490,y=280)
Label(raiz, text="28 Angel Hyde", fon=6, bg="Gold",fg="black").place(x=490,y=340)



boton = ttk.Button(raiz,text="REGISTRATE",command=insertar).place(x=299, y=500)

raiz.mainloop()