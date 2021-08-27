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
#PANTALLA WALESKA 

#CONEXION 
def factura():
    raiz.destroy()
    import Registroadulto_mayor

def medicamentos():
    raiz.destroy()
    import pantalla

    



raiz=Tk()
raiz.title("Registro cliente_WALESKA")
raiz.resizable(1,1)
raiz.geometry("745x1000")
raiz.config(bg="RoyalBlue")
raiz.resizable(0,0)


Label(raiz, text="FARMACIA SALUD Y VIDA-REGISTRO DEL CLIENTE", fon=10, bg="#FFD700").place(x=155,y=10)
Label(raiz, text="Telefono: 2772-9944  2771-0023  9876-5433", fon=10, bg="#FFD700",fg="black").place(x=200,y=50)
Label(raiz, text="Ingresa tu datos", fon=10, bg="#FFD700",fg="black").place(x=250,y=89)
Label(raiz, text="Barrio San Blas,esquina opuesta a Gasolinera UNO", fon=10, bg="#FFD700",fg="black").place(x=120,y=130)
Label(raiz, text="Descuentos:", fon=10, bg="sky blue",fg="red").place(x=0,y=345)
Label(raiz, text="NOTA: Si es adulto mayor de 60 años registrese de un solo y si no solo seleccione sus medicamentos ", fon=10, bg="sky blue",fg="black").place(x=0,y=370)

nombre=Label(raiz, text="Nombre del Cliente: ", fon=10, bg="RoyalBlue")
nombre.config(fg="black") 
nombre.place(x=0,y=200)
Entry(raiz).place(x=150,y=210)
nombre=Label(raiz, text="Apellidos: ", fon=10, bg="RoyalBlue")
nombre.config(fg="black") 
nombre.place(x=340,y=200)
Entry(raiz).place(x=420,y=210)
nombre=Label(raiz, text="ciudad: ", fon=10, bg="RoyalBlue")
nombre.config(fg="black") 
nombre.place(x=0,y=280)
Entry(raiz).place(x=60,y=290,width=270,height=30)
nombre=Label(raiz, text="Provincia: ", fon=10, bg="RoyalBlue")
nombre.config(fg="black") 
nombre.place(x=340,y=280)
Entry(raiz).place(x=420,y=290)
boton = ttk.Button(text="Mayor de edad")
boton.place(x=25, y=400)
nombre=Label(raiz, text="recidencia: ", fon=10, bg="RoyalBlue")
nombre.config(fg="red") 
nombre.place(x=10,y=490)
Entry(raiz).place(x=100,y=500,width=500,height=30)
nombre=Label(raiz, text="Telefono: ", fon=10, bg="RoyalBlue")
nombre.config(fg="black") 
nombre.place(x=10,y=579)
Entry(raiz).place(x=85,y=585,width=190,height=20)
nombre=Label(raiz, text="Correo Electronico: ", fon=10, bg="RoyalBlue")
nombre.config(fg="black") 
nombre.place(x=10,y=630)
Entry(raiz).place(x=150,y=630,width=500,height=25)


#BOTONES 
boton = ttk.Button(raiz,text="Mayor de edad",command=factura).place(x=25, y=400)
boton = ttk.Button(text="Selecionar medicamentos:",command=medicamentos).place(x=190, y=400)

raiz.mainloop()
