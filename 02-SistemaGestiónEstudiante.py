import tkinter as tk
import sqlite3
from tkinter import messagebox

def bdEstudiantes():
    conn = sqlite3.connect("dbEstudiantes.db")  # Creo la Base de Datos para guardar los datos de Estudiantes
    cursor = conn.cursor()
    # A continuación, creo la tabla estudiantes, con los atributos id, nombre, edad y carrera
    cursor.execute(  
        """
        CREATE TABLE IF NOT EXISTS estudiantes (
            id_Estudiante INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL,
            carrera TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

# Esta función def lo usaré para mostrar los datos del estudiante, esto en un listbox
def mostrarEstudiantes():
    listbox.delete(0, tk.END)
    conn = sqlite3.connect("dbEstudiantes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudiantes")
    for fila in cursor.fetchall():
        listbox.insert(tk.END, f"ID: {fila[0]}  Estudiante: {fila[1]} ;  Edad: {fila[2]} ; Carrera: {fila[3]}")
    conn.close()
    
# Esta otra función para ir guardando los datos a medida que ingrese más datos
def guardarEstudiante():
    nombreEstudiante = entry_nombre.get()
    edadEstudiante = entry_edad.get()
    carreraEstudiante = entry_carrera.get()
    if nombreEstudiante and edadEstudiante.isdigit() and carreraEstudiante:
        conn = sqlite3.connect("dbEstudiantes.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO estudiantes(nombre, edad, carrera) VALUES (?,?,?)", (nombreEstudiante, int(edadEstudiante), carreraEstudiante))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito","Exitos al guardar los datos del usuario!")
        entry_nombre.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
        entry_carrera.delete(0,tk.END)
        
    else:
        messagebox.showerror("Error", "Ingrese un nombre, una edad y su carrera válida")

# Función para buscar estudiante por nombre  
def buscarEstudiantes():
    nombre = entry_BuscarEstudiante.get()
    listbox.delete(0, tk.END)
    conn = sqlite3.connect("dbEstudiantes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudiantes WHERE nombre LIKE ?", ("%" + nombre + "%",))
    filas = cursor.fetchall()
    for fila in filas:
        listbox.insert(tk.END, f"ID: {fila[0]} | Estudiante: {fila[1]} | Edad: {fila[2]} | Carrera: {fila[3]}")
    conn.close()
        
def modificarEstudiante():
        id_Estudiante = entry_ModificarEstudiante.get()
        nuevaCarrera = entry_nuevaCarrera.get()
        if id_Estudiante.isdigit() and nuevaCarrera:
            conn = sqlite3.connect("dbEstudiantes.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE estudiantes SET carrera = ? WHERE id_Estudiante = ?", (nuevaCarrera, int(id_Estudiante)))
            conn.commit()
            conn.close()
            messagebox.showinfo("ACTUALIZADO"," Los datos, la carrera que estudia el estudiante ha sido actuailizado correctamente!")
        else:
            messagebox.showerror("ERROR", "Verifique sus datos por favor!!!")
# Inicio la ventana 
window = tk.Tk()
window.title("Sistema de Gestión de Estudiantes")
window.geometry("800x800")
window.config(bg="#d0f0c0")
bdEstudiantes()
        
# Creo los labels para ingresar los datos

#Para ingresar el  nombre
labelNombre = tk.Label(window, text="Ingrese su nombre por favor!")
labelNombre.pack(pady=(10,0))
entry_nombre = tk.Entry(window, font=("Times New Roman", 15))
entry_nombre.insert(0, "")
entry_nombre.pack(pady=(0,10))

# Para ingresar la edad
labelEdad = tk.Label(window, text="Ingrese su edad por favor!")
labelEdad.pack(pady=(10,0))
entry_edad = tk.Entry(window, font=("Times New Roman", 15))
entry_edad.insert(0, "")
entry_edad.pack(pady=(0,10))

# Para ingresar la carrera
labelCarrera = tk.Label(window, text="Ingrese la carrera que está cursando por favor!")
labelCarrera.pack(pady=(10,0))
entry_carrera = tk.Entry(window, font=("Times New Roman", 15))
entry_carrera.insert(0, "")
entry_carrera.pack(pady=(0,10))

labelBotonAgregarEstudiante = tk.Label(window, text="Agregar Estudiante")
labelBotonAgregarEstudiante.pack(pady=(10,0))
tk.Button(window, text="Agregar", command=guardarEstudiante).pack(pady=(0,10))

# Para buscar al estudiante por nombre
labelBuscarstudiante = tk.Label(window, text="Buscar Estudiante por nombre, ingrese el nombre que desee buscar")
labelBuscarstudiante.pack(pady=(10,0))
entry_BuscarEstudiante = tk.Entry(window)
entry_BuscarEstudiante.pack()
tk.Button(window, text="Buscar", command=buscarEstudiantes).pack(pady=(0,10))

# Para modificar la carrera del estudiante
labelModificarEstudiante = tk.Label(window, text="Modificar carrera por id del Estudiante")
labelModificarEstudiante.pack()
entry_ModificarEstudiante = tk.Entry(window)
entry_ModificarEstudiante.pack()

labelNuevaCarrera = tk.Label(window, text="Ingrese la carrera a actualizar").pack()
entry_nuevaCarrera = tk.Entry(window)
entry_nuevaCarrera.pack()

tk.Button(window, text="Modificar", command=modificarEstudiante).pack(pady=(0,10))


    
# List Box 
listbox = tk.Listbox(window, width=80)
listbox.pack()
tk.Button(window, text="Mostrar todos los estudiantes", command=mostrarEstudiantes ).pack()

window.mainloop()