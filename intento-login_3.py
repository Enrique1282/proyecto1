import tkinter
from tkinter import*
from tkinter import messagebox
import pymysql

def menu_pantalla():
    global pantalla
    pantalla = Tk()
    pantalla.geometry("300x380")
    pantalla.title("Benvindo")

    Label(text = "Acceso al sistema", bg= "navy", fg= "white", width= "300", height= "3", font=("calibri",15)).pack()
    Label(text= "").pack()

    Button(text= "Iniciar Sesión", height= "3", width= "30", command= inicio_sesion).pack()
    Label(text= "").pack()
    Button(text= "Registrarse", height= "3", width= "30").pack()

    pantalla.mainloop()

def inicio_sesion():
    global pantalla_1
    pantalla_1 = Toplevel(pantalla)
    pantalla_1.geometry("400x250")
    pantalla_1.title("Inicio de Sesión")
    
    Label(pantalla_1,text="Por favor ingrese su Usuario y Contraseña")
    Label(pantalla_1, text= "").pack()

    global nombreusuario_verify
    global contrasenausuario_verify

    nombreusuario_verify = StringVar()
    contrasenausuario_verify = StringVar()

    global nombre_usuario_entry
    global contrasena_usuario_entry

    Label(pantalla_1,text= "Usuario").pack()
    nombre_usuario_entry = Entry(pantalla_1, textvariable= nombreusuario_verify)
    nombre_usuario_entry.pack()
    Label(pantalla_1).pack()
    

    Label(pantalla_1, text= "Contraseña").pack()
    contrasena_usuario_entry = Entry(pantalla_1, textvariable= contrasenausuario_verify)
    contrasena_usuario_entry.pack()
    Label(pantalla_1).pack()

    Button(pantalla_1, text= "Iniciar Sesión").pack()

menu_pantalla()