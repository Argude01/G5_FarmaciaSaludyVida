from tkinter import *
import tkinter as tk
from tkinter import ttk
import os

#PANTLLA ANNETTE

def Factura():
    raiz.destroy()
    import PantallaFarmacia

raiz=Tk()
raiz.title("R E C E T A_ANNETTE ")
raiz.resizable(1,1)
raiz.geometry("790x650")
raiz.config(bg="white smoke")
raiz.resizable(0,0)
Label(raiz, text="HOSPITAL SALUD Y VIDA", fon=100, bg="white smoke").place(x=30,y=10)

nombre=Label(raiz, text="Barrio San Blas,esquina opuesta a Gasolinera UNO´´ ", fon=5, bg="white smoke")
nombre.config(fg="black") 
nombre.place(x=5,y=80)

nombre=Label(raiz, text="Teléfono: 2772-9944  2771-0023  9876-5433", fon=5, bg="white smoke")
nombre.config(fg="black") 
nombre.place(x=5,y=50)

nombre=Label(raiz, text="Codigo:UR-FO-09 ", fon=5, bg="white smoke")
nombre.config(fg="black") 
nombre.place(x=505,y=10)


nombre=Label(raiz, text="Versión 01", fon=5, bg="white smoke")
nombre.config(fg="black") 
nombre.place(x=505,y=40)


nombre=Label(raiz, text="Nombre del paciente: ", fon=5, bg="white smoke")
nombre.config(fg="black") 
nombre.place(x=5,y=145)
Entry(raiz).place(x=70,y=208)

nombre=Label(raiz, text="N° de Identidad : ", fon=5, bg="white smoke")
nombre.config(fg="black") 
nombre.place(x=5,y=175)
Entry(raiz).place(x=70,y=236)

nombre=Label(raiz, text="Edad : ", fon=5, bg="white smoke")
nombre.config(fg="black") 
nombre.place(x=5,y=205)
Entry(raiz).place(x=170,y=150)

nombre=Label(raiz, text="Fecha : ", fon=5, bg="white smoke")
nombre.config(fg="black") 
nombre.place(x=5,y=235)
Entry(raiz).place(x=170,y=177)

nombre=Label(raiz, text="Teléfono: ", fon=5, bg="white smoke")
nombre.config(fg="black") 
nombre.place(x=425,y=145)
Entry(raiz).place(x=500,y=150)

nombre=Label(raiz, text="Dirección: ", fon=5, bg="white smoke")
nombre.config(fg="black") 
nombre.place(x=425,y=175)
Entry(raiz).place(x=502,y=180)

nombre=Label(raiz, text="Genero: ", fon=5, bg="white smoke")
nombre.config(fg="black") 
nombre.place(x=425,y=205)

nombre=Label(raiz, text="FÓRMULA MÉDICA ", fon=105, bg="white smoke")
nombre.config(fg="black") 
nombre.place(x=300,y=285)

nombre=Label(raiz, text="Firma y Sello del Médico", fon=5, bg="white smoke")
nombre.config(fg="black") 
nombre.place(x=60,y=550)
Entry(raiz).place(x=90,y=520)

radio = IntVar
radio1 = IntVar

R1 = Radiobutton(raiz, text="Masculino", variable=radio, value=1, bg="white smoke", fg="coral")
R1.pack(anchor=W)
R1.place(x=500, y=205)

radio = IntVar
radio1 = IntVar

R2 = Radiobutton(raiz, text="Femenino", variable=radio, value=2, bg="white smoke",fg="coral")
R2.pack(anchor=W)
R2.place(x=595, y=205)

Boton= Button(raiz,text="Factura", command=Factura, fon=15, height = 3, width = 20, bg="#FFD700").place(x=585,y=550)

raiz.mainloop()
