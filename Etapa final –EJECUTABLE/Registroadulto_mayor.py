from tkinter import *
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkFont
import os
# STEPHANIE ACOSTA 



def factura():
    raiz.destroy()
    import PantallaFarmacia


def descuento():
    Desc.set(precio*0.30)

raiz=Tk()
raiz.title("Registro adulto mayor")
raiz.resizable(1,1)
raiz.geometry("745x1000")
raiz.config(bg="RoyalBlue")
raiz.resizable(0,0)
Label(raiz, text="FARMACIA SALUD Y VIDA-ADULTO MAYOR", fon=10, bg="#FFD700").place(x=220,y=10)
Label(raiz, text="Telefono: 2772-9944  2771-0023  9876-5433", fon=10, bg="Gold",fg="black").place(x=200,y=60)
Label(raiz, text="Ingresa sus datos", fon=10, bg="Gold",fg="black").place(x=310,y=89)
Label(raiz, text=" Barrio San Blas,esquina opuesta a Gasolinera UNO", fon=10, bg="Gold",fg="black").place(x=180,y=130)


#listas desplegable
lista_desplegable = ttk.Combobox(raiz,width=17)
lista_desplegable.place(x=140,y=399,width=300,height=30)

opciones = ["insulina","amoxixilina","acetaminofen","enamtuim","tazarol","ibuprofeno","dexamentazona","aspirina","omeprazol","paracetamol","espamotil"]

#insertar valores.
lista_desplegable['value']=opciones

nombre=Label(raiz, text="Ingrese su nombre: ", fon=10, bg="RoyalBlue")
nombre.config(fg="black") 
nombre.place(x=5,y=190)
Entry(raiz).place(x=150,y=193,width=90,height=30)
nombre=Label(raiz, text="Edad: ", fon=10, bg="RoyalBlue")
nombre.config(fg="black") 
nombre.place(x=300,y=195)
Entry(raiz).place(x=390,y=194)

nombre=Label(raiz, text="Sexo: ", fon=10, bg="RoyalBlue")
nombre.config(fg="black") 
radio = IntVar
radio1 = IntVar

R1 = Radiobutton(raiz, text="Masculino", variable=radio, value=1, bg="white smoke", fg="coral")
R1.pack(anchor=W)
R1.place(x=199, y=299)

radio = IntVar
radio1 = IntVar

R2 = Radiobutton(raiz, text="Femenino", variable=radio, value=2, bg="white smoke",fg="coral")
R2.pack(anchor=W)
R2.place(x=100, y=300)
nombre.place(x=5,y=290)

nombre=Label(raiz, text="DNI del cliente: ", fon=10, bg="RoyalBlue")
nombre.config(fg="black") 
nombre.place(x=350,y=290)
Entry(raiz).place(x=470,y=298,width=200,height=30)

nombre=Label(raiz, text="Medicamentos: ", fon=10, bg="RoyalBlue")
nombre.config(fg="black") 
nombre.place(x=10,y=390)

precio=Label(raiz, text="Precio del producto: ", fon=10, bg="RoyalBlue")
precio.config(fg="black") 
precio.place(x=10,y=460)
Entry(raiz).place(x=199,y=460,width=199,height=20)

Desc=Label(raiz ,text="Descuento 30%: ", fon=10, bg="RoyalBlue")
Desc.config(fg="black") 
Desc.place(x=10,y=490)
Entry(raiz).place(x=150,y=500,width=300,height=20)
boton_descuenta= Button(raiz,text="descuento", command= descuento, height = 2, width = 20,bg="#FFD700" ).place(x=399,y=450)


 
nombre=Label(raiz, text="Es cliente frecuente (si,no): ", fon=10, bg="RoyalBlue")
nombre.config(fg="black") 
nombre.place(x=10,y=550)
Entry(raiz).place(x=200,y=550,width=100,height=20)



nombre=Label(raiz, text="Puntos Acumulados: ", fon=10, bg="RoyalBlue")
nombre.config(fg="black") 
nombre.place(x=10,y=590)
Entry(raiz).place(x=200,y=600,width=300,height=20)

          
boton44= Button(raiz,text="FACTURA", command= factura, height = 2, width = 20,bg="#FFD700" ).place(x=500,y=650)


raiz.mainloop()
