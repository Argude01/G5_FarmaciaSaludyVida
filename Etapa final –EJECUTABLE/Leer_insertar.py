from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from mysql.connector import cursor
import demo_database
import time
import os
import mysql.connector

def CLIENTE():
    window.destroy()
    import clientes

fecha=(time.strftime("%d/%m/%y"))
hora=(time.strftime('%I:%M:%S'))
#pantalla keydi

window = Tk()
frame_app = Frame(window,width=11, height=11)
window.title('FARMACIA_KEYDI')
window.resizable(0,0)
my_table = ttk.Treeview(window)
frame_app.pack()



nombre_farmacia = StringVar()
ubicacion = StringVar()
telefono_farmcia= StringVar()
correo = StringVar()

class MyDatabase:
    # PASO 3: Crear la función "open_connection", 
    #         para abrir la conexión y tener acceso a la base de datos correspondiente
    def open_connection(self):
        connection =mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="db_demo")
        return connection

def insert_db(self, nombre_farmacia,ubicacion,telefono_farmcia,correo):
            my_connection = self.open_connection()
            cursor = my_connection.cursor()
            query = "INSERT INTO tbl_registros_farmacia(NOMBRE_FARMACIA,UBICACION,TELEFONO_FARMCIA_CORREO) VALUES (%s,%s,%s,%s)"
            data = (nombre_farmacia,ubicacion,telefono_farmcia,correo)
            cursor.execute(query, data)
            for fila in cursor:
                nombre_farmacia = fila[0]  
                ubicacion= fila[1]
                telefono_farmcia = fila[2]  
                correo= fila[3]
                print(fila)
                print(fila[0])
            my_connection.commit()
            my_connection.close()

   

def crear():
    nombre_farmacia = entry_nombre_farmacia.get()
    ubicacion = entry_ubicacion.get()
    telefono_farmcia= entry_telefono_farmcia.get()
    correo = entry_correo.get()
    demo_db = demo_database.MyDatabase()
    demo_db.insert_db(nombre_farmacia,ubicacion,telefono_farmcia,correo)  


connection =mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="db_demo")
   

my_table['columns'] = ('NOMBRE_FARMACIA','UBICACION','TELEFONO_FARMCIA','CORREO')

my_table.column('#0', width=120, minwidth=50)
my_table.column('NOMBRE_FARMACIA', anchor=W, width=120)
my_table.column('UBICACION', anchor=W, width=120)
my_table.column('TELEFONO_FARMCIA', anchor=W, width=120)
my_table.column('CORREO', anchor=W, width=120)


my_table.heading('#0', text='ID_CAMPO', anchor=W)
my_table.heading('NOMBRE_FARMACIA', text='NOMBRE_FARMACIA', anchor=W)
my_table.heading('UBICACION', text='UBICACION', anchor=W)
my_table.heading('TELEFONO_FARMCIA', text='TELEFONO_FARMCIA', anchor=W)
my_table.heading('CORREO', text='CORREO', anchor=W)

cursor = connection.cursor()
cursor.execute("SELECT NOMBRE_FARMACIA, UBICACION, TELEFONO_FARMCIA, CORREO FROM TBL_REGISTROS_FARMACIA")
registro=0   

my_table = ttk.Treeview(window)
    

for fila in cursor:
    registro=registro+1
    print(str(registro) + "-"+str(fila))
    nombre_farmacia = fila[0]  
    ubicacion = fila[1]
    telefono_farmcia = fila[2]
    correo = fila[3]
   
    my_table.insert(parent="", index="end", iid=registro, text=str(registro),
        values=(nombre_farmacia, ubicacion,telefono_farmcia,correo))
connection.close() 


my_table.place(x=160, y=460)

frame_navbar = Frame(frame_app, width=900, height=100,bg="RoyalBlue")
frame_navbar.grid(row=0, column=0)
frame_title = Frame(frame_app, width=900, height=120,bg="RoyalBlue")
frame_title.grid(row=1, column=0)
frame_options = Frame(frame_app, width=900, height=500,bg="RoyalBlue")
frame_options.grid(row=2, column=0)

title = Label(frame_navbar,
              bg="Gold",
              text=" FARMACIA SALUD Y VIDA",
              font=("Modern Love Caps", "19"))
title.place(x=300, y=20)
title1 = Label(frame_navbar,
              bg="Gold",
              text="  Barrio San Blas,esquina opuesta a Gasolinera UNO",
              font=("Modern Love Caps", "19"))
title1.place(x=100, y=70)

title2 = Label(frame_title,
               bg="Gold",
              text="¡PEDIDOS A DOMICILIO!", 
              font=("KG What A Time", "14", "bold"),
              justify=LEFT)
title2.place(x=350, y=80)


title3 = Label(frame_title,
               bg="Gold",
              text="SI USTED ES EMPLEADO REGISTRESE SI NO (PASE A REGISTRO CLIENTE:", 
              font=("KG What A Time", "12"),
              justify=LEFT)
title3.place(x=20, y=40)



frame_form = Frame(frame_options, width=870, height=250,bg="RoyalBlue")
frame_form.place(x=25, y=5)
label_nombre_farmacia = Label(frame_form, 
              text="NOMBRE_FARMACIA:",
              font=("KG What A Time", "14", "bold"),
              fg="black",
              bg="RoyalBlue")
label_nombre_farmacia.place(x=10, y=10)
entry_nombre_farmacia = Entry(frame_form, justify=LEFT, width=25, 
             font=("KG What A Time", "14"))
entry_nombre_farmacia.place(x=15, y=50)


label_ubicacion = Label(frame_form, 
              text="UBICACION:",
              font=("KG What A Time", "14", "bold"),
              fg="black",
              bg="RoyalBlue")
label_ubicacion.place(x=390, y=10)
entry_ubicacion = Entry(frame_form, justify=LEFT, width=25, 
                font=("KG What A Time", "14"))
entry_ubicacion.place(x=420, y=50)

label_telefono_farmcia = Label(frame_form, 
              text="TELEFONO_FARMACIA:",
              font=("KG What A Time", "14", "bold"),
              fg="black",
              bg="RoyalBlue")
label_telefono_farmcia.place(x=10, y=100)
entry_telefono_farmcia = Entry(frame_form, justify=LEFT, width=25, 
                font=("KG What A Time", "14"))
entry_telefono_farmcia.place(x=30, y=130)


label_correo = Label(frame_form, 
              text="CORREO:",
              font=("KG What A Time", "14", "bold"),
              fg="black",
              bg="RoyalBlue")
label_correo.place(x=390, y=100)
entry_correo = Entry(frame_form, justify=LEFT, width=25, 
                font=("KG What A Time", "14"))
entry_correo.place(x=420, y=130)


#messagebox.showinfo(message="Te has registrado a nuetra farmacia", title="SALUD Y VIDA")

fon=Label()
fon.place(x=780,y=40)
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
fecha=Label(window, font=10, bg="#FFD700",text="Fecha: "+rr)
fecha.config(fg="black") 
fecha.place(x=660,y=40)

button_agregar = Button(frame_form, text="crear", 
                        font=("KG What A Time", "14", "bold"),
                        command=crear, bg="Gold", fg="black")
button_agregar.place(x=410, y=180)


button_agregar = ttk.Button(window,text="REGISTRO CLIENTE",command=CLIENTE)
button_agregar.place(x=290, y=399)

connection =mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="db_demo")

my_table['columns'] = ('NOMBRE_FARMACIA','UBICACION','TELEFONO_FARMCIA','CORREO')

my_table.column('#0', width=120, minwidth=50)
my_table.column('NOMBRE_FARMACIA', anchor=W, width=120)
my_table.column('UBICACION', anchor=W, width=120)
my_table.column('TELEFONO_FARMCIA', anchor=W, width=120)
my_table.column('CORREO', anchor=W, width=120)


my_table.heading('#0', text='ID_CAMPO', anchor=W)
my_table.heading('NOMBRE_FARMACIA', text='NOMBRE_FARMACIA', anchor=W)
my_table.heading('UBICACION', text='UBICACION', anchor=W)
my_table.heading('TELEFONO_FARMCIA', text='TELEFONO_FARMCIA', anchor=W)
my_table.heading('CORREO', text='CORREO', anchor=W)

cursor = connection.cursor()
cursor.execute("SELECT NOMBRE_FARMACIA, UBICACION, TELEFONO_FARMCIA, CORREO FROM TBL_REGISTROS_FARMACIA")
registro=0   

my_table = ttk.Treeview(window)
    

for fila in cursor:
    registro=registro+1
    print(str(registro) + "-"+str(fila))
    nombre_farmacia = fila[0]  
    ubicacion = fila[1]
    telefono_farmcia = fila[2]
    correo = fila[3]
   
    my_table.insert(parent="", index="end", iid=registro, text=str(registro),
        values=(nombre_farmacia, ubicacion,telefono_farmcia,correo))
connection.close() 



window.mainloop()
