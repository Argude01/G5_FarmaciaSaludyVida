from tkinter import *
import os
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
import sqlite3
import os
import time

#PANTALLA GUILLERMO


def RECETA():
    raiz.destroy()
    import Receta




raiz=Tk()
raiz.title("MEDICAMENTOS_GUILLERMO")
raiz.resizable(1,1)
raiz.geometry("790x800")
raiz.config(bg="RoyalBlue",)
raiz.resizable(0,0)
Label(raiz, text="FARMACIA SALUD Y VIDA-ADULTO MAYOR", fon=10, bg="#FFD700").place(x=220,y=10)
Label(raiz, text="Telefono: 2772-9944 2771-0023 9876-5433", fon=10, bg="Gold",fg="black").place(x=200,y=60)
Label(raiz, text="Ingresa sus datos", fon=10, bg="Gold",fg="black").place(x=310,y=89)
Label(raiz, text= " Barrio San Blas,esquina opuesta a Gasolinera UNO", fon=10, bg="Gold",fg="black").place(x=180,y=130)

#listas desplegable
lista_desplegable = ttk.Combobox(raiz,width=20)
lista_desplegable.place(x=330,y=440)

opciones = ["Insulina L.300","Amoxixilina 2c/u,caja L.20","Acetaminofen 2c/u, caja L.120","Enamtuim L.150","Tazarol L.234","Ibuprofeno 2c/u,caja L.120","Dexamentazona L.130","Aspirina 3c/u,caja L.97,en polvo L.20","Omeprazol L.340","Paracetamol L. 235","Espamotil 4C/U, caja L.110"]

#insertar valores.
lista_desplegable['value']=opciones


lista_desplegable = ttk.Combobox(raiz,width=20)
lista_desplegable.place(x=56,y=310,width=190,height=30)

opciones = ["Pastillas","Jarabe","Inyectables","Espray","Crema","Enpolvo"]

#insertar valores.
lista_desplegable['value']=opciones

lista_desplegable = ttk.Combobox(raiz,width=20)
lista_desplegable.place(x=390,y=225,width=190,height=30)

opciones = ["Colposan","Clevium","Henie","Clivan","xirmen","Etoricox"]

#insertar valores.
lista_desplegable['value']=opciones



lista_desplegable['value']=opciones

lista_desplegable = ttk.Combobox(raiz,width=20)
lista_desplegable.place(x=390,y=310,width=190,height=30)

opciones = ["En tabletas","Bote","Sobresitos","caja","Anpollas"]

#insertar valores.
lista_desplegable['value']=opciones



nombre=Label(raiz, text="Principio Activo: ", fon=10, bg="yellow")
nombre.config(fg="black") 
nombre.place(x=50,y=195)
Entry(raiz).place(x=55,y=225,width=190,height=30)
nombre2=Label(raiz, text="Marca Registrada: ", fon=10, bg="yellow")
nombre2.config(fg="black") 
nombre2.place(x=360,y=195)


nombre3=Label(raiz, text="Forma: ", fon=10, bg="yellow")
nombre3.config(fg="black") 
nombre3.place(x=50,y=280)


nombre4=Label(raiz, text="Presentacion: ", fon=10, bg="yellow")
nombre4.config(fg="black") 
nombre4.place(x=360,y=280)


nombre5=Label(raiz, text="Medicamentos: ", fon=150, bg="green")
nombre5.config(fg="black") 
nombre5.place(x=330,y=400)

nombre6=Label(raiz, text="Buscar por: ", fon=10, bg="yellow")
nombre6.config(fg="black") 
nombre6.place(x=50,y=500)
Entry(raiz).place(x=150,y=500,width=200,height=30)

boton44= Button(raiz,text="RECETA", command=RECETA, height = 2, width = 20,bg="#FFD700").place(x=630,y=410)



raiz.mainloop()