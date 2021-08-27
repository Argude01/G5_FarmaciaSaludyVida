from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
from tkinter import messagebox
import time

fecha=(time.strftime("%d/%m/%y"))
hora=(time.strftime('%I:%M:%S'))


# YEIRI

def factura(self):
    raiz.destroy()
    os.system("PantallaFarmacia.py")


def regresar():
    valor=messagebox.showinfo("PAGO","PAGADO")
    messagebox.showinfo("CANCELADO", "GRACIAS POR PREFERIRNOS")
    raiz.destroy()




raiz=Tk()
raiz.title("FACTURA_YEIRI")
raiz.resizable(1,1)
raiz.geometry("530x550")
raiz.config(bg="RoyalBlue")
raiz.resizable(0,0)
Label(raiz, text="SALUD  Y   VIDA", fon=20, bg="#FFD700").place(x=210,y=10)
Label(raiz, text="**FACTURACION**", fon=20, bg="#FFD700").place(x=200,y=50)



nombre=Label(raiz, text="RCP: ", fon=10, bg="RoyalBlue")
nombre.config(fg="black") 
nombre.place(x=90,y=125)

Entry(raiz).place(x=255,y=132)

nombre=Label(raiz, text="RAZON SOCIAL: ", fon=10, bg="RoyalBlue")
nombre.config(fg="black") 
nombre.place(x=90,y=165)

Entry(raiz).place(x=255,y=172)

nombre=Label(raiz, text="PAIS: ", fon=10, bg="RoyalBlue")
nombre.config(fg="black") 
nombre.place(x=90,y=205)

Entry(raiz).place(x=255,y=212)

nombre=Label(raiz, text="ESTADO: ", fon=10, bg="RoyalBlue")
nombre.config(fg="black") 
nombre.place(x=90,y=245)

Entry(raiz).place(x=255,y=252)

nombre=Label(raiz, text="COLONIA: ", fon=10, bg="RoyalBlue")
nombre.config(fg="black") 
nombre.place(x=90,y=285)

Entry(raiz).place(x=255,y=292)

nombre=Label(raiz, text="# INT: ", fon=10, bg="RoyalBlue")
nombre.config(fg="black") 
nombre.place(x=90,y=325)

Entry(raiz).place(x=255,y=332)

nombre=Label(raiz, text="E-MAIL: ", fon=10, bg="RoyalBlue")
nombre.config(fg="black") 
nombre.place(x=90,y=365)

Entry(raiz).place(x=255,y=372)

nombre=Label(raiz, text="TOTAL: ", fon=10, bg="RoyalBlue")
nombre.config(fg="black") 
nombre.place(x=90,y=405)

Entry(raiz).place(x=255,y=412)

fon=Label()

fon=Label()
fon.place(x=10,y=40)
fon['font']="Helvetica"
fon['bg']='#FFD700'
def tic():
    fon['text']="Hora: "+time.strftime('%I:%M:%S')
tic()

def tac():
    tic()
    fon.after(1000,tac)
tac()

rr=(time.strftime("%d/%m"))
fecha=Label(raiz, font=10, bg="#FFD700",text="Fecha: "+rr)
fecha.config(fg="black") 
fecha.place(x=10,y=70)


boton44= Button(raiz,text="CANCELADO", command=regresar, height = 2, width = 20,bg="#FFD700").place(x=170,y=490)

raiz.mainloop()








