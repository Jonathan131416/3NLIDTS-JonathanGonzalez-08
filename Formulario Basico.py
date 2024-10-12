# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 23:57:32 2024

@author: Antonio
"""

import tkinter as tk
from tkinter import messagebox
import re
import mysql.connector

def insertarRegistro(nombres, apellidos, edad, estatura, telefono, genero):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="Salinas031",
            database="Formulario"
        )
        
        cursor = conexion.cursor()
        query = "INSERT INTO registros (Nombre, Apellidos, Telefono, Estatura, Edad, Genero) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (nombres, apellidos, telefono, estatura, edad, genero)
        cursor.execute(query, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        messagebox.showinfo("Información", "Datos guardados en la base de datos con éxito.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al insertar los datos: {err}")
        
def limpiar_campos():
    tbNombre.delete(0,tk.END)
    tbApellidos.delete(0,tk.END)
    tbEdad.delete(0,tk.END)   
    tbEstatura.delete(0,tk.END)
    tbTelefono.delete(0,tk.END)
    var_genero.set(0)
    
def borrar_fun():
    limpiar_campos()
    
def es_entero_valido(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False
    
def es_decimal_valido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False
    
def es_entero_valido_de_10_digitos(valor):
    return valor.isdigit() and len(valor)==10

def es_texto_valido(valor):
    return bool(re.match(r"^[a-zA-Z\s]+$", valor))    
    
def guardar_valores():
    nombres= tbNombre.get()
    apellidos = tbApellidos.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()
    telefono = tbTelefono.get()
    genero = ""
    if var_genero.get()==1:
        genero= "Hombre"
    elif var_genero.get()==2:
        genero="Mujer"
    if (es_entero_valido(edad)and es_decimal_valido(estatura)and  es_entero_valido_de_10_digitos(telefono)and es_texto_valido(nombres) and es_texto_valido(apellidos)):
        datos = "Nombres:"+ nombres + "\n" + "Apellidos: " + apellidos +"\n" + "Edad:" + edad + "años\n" + "Estatura:" + estatura +"\n"+"Telefono:" + telefono + "\n" + "Genero:"+ genero + "\n" 
        with open("Formulario Basico.txt","a") as archivo:
            archivo.write(datos+"\n\n")    
        insertarRegistro(nombres, apellidos, edad, estatura, telefono, genero)
        messagebox.showinfo("Informacion", "Datos Guardados con exito: \n\n" + datos)
        
    else: 
        messagebox.showinfo("ERROR", "Los datos contienen formatos no válidos:\n\n")

    
ventana = tk.Tk()
ventana.geometry("520x500")
ventana.title("Formulario Basico")
var_genero = tk.IntVar()

lbNombre=tk.Label(ventana,text="Nombres:")
lbNombre.pack()
tbNombre=tk.Entry()
tbNombre.pack()
lbApellidos=tk.Label(ventana,text="Apellidos:")
lbApellidos.pack()
tbApellidos=tk.Entry()
tbApellidos.pack()
lbTelefono=tk.Label(ventana,text="Telefono:")
lbTelefono.pack()
tbTelefono=tk.Entry()
tbTelefono.pack()
lbEdad=tk.Label(ventana,text="Edad:")
lbEdad.pack()
tbEdad=tk.Entry()
tbEdad.pack()
lbEstatura=tk.Label(ventana,text="Estatura:")
lbEstatura.pack()
tbEstatura=tk.Entry()
tbEstatura.pack()
lbGenero=tk.Label(ventana,text="Genero:")
lbGenero.pack()
rbHombre=tk.Radiobutton(ventana,text="Hombre",variable=var_genero,value=1)
rbHombre.pack()
rbMujer=tk.Radiobutton(ventana,text="Mujer",variable=var_genero,value=2)
rbMujer.pack()
    
btnBorrar = tk.Button(ventana, text="Borrar valores", command=borrar_fun)
btnBorrar.pack()
btnGuardar = tk.Button(ventana, text="Guardar",command=guardar_valores)
btnGuardar.pack()
    
ventana.mainloop()