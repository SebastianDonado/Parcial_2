import tkinter as tk
from tkinter import messagebox
from Conexion_firebase import guardar_libro, obtener_libros, actualizar_estado
from funciones import crear_libro, buscar_libros

def registrar():
    libro = crear_libro(e_titulo.get(), e_autor.get(), var_categoria.get(), e_codigo.get())  #creamos un diccionario
    guardar_libro(libro)   # se guarda el libro en la base de datos
    messagebox.showinfo("Éxito", "Libro registrado")   # mensaje de exito

    # Limpiar campos de entrada
    e_titulo.delete(0, tk.END)
    e_autor.delete(0, tk.END)
    e_codigo.delete(0, tk.END)


def consultar():
    consulta = e_busqueda.get()  # Leer lo que escribió el usuario
    libros = obtener_libros()    # Traer todos los libros desde Firebase
    encontrados = buscar_libros(libros, consulta)  # Buscar por título con la funcion buscar_libros de funciones.py

    t_resultado.delete("1.0", tk.END)  # Limpiar el área de resultados
#Con esta estructura se verifica si se encontró algún libro
    if not encontrados:
        messagebox.showerror("No encontrado", "No se encontró ningún libro con ese título o autor.")
    else:
        for l in encontrados:         #Aqui se itera sobre los libros encontrados para saber su estado
            estado = "Disponible" if l["disponible"] else "Prestado"
            t_resultado.insert(tk.END, f'{l["titulo"]} - {l["autor"]} [{estado}]\n')

    e_busqueda.delete(0, tk.END)  # Aquí se borra la entrada de texto correctamente

def limpiar_resultado():
    t_resultado.delete("1.0", tk.END)    # Limpiar el área de resultados

def prestar():
    codigo = e_codigo_prestamo.get()
    libros = obtener_libros()

    for libro in libros:
        if libro["codigo"] == codigo:
            libro["disponible"] = False
            actualizar_estado(libro["codigo"], False)
            messagebox.showinfo("Préstamo", "Libro prestado con éxito.")
            e_codigo_prestamo.delete(0, tk.END)
            return

    # Si no encontró el código
    messagebox.showerror("Error", f"No se encontró ningún libro con el código: {codigo}")

def devolver():
    codigo = e_codigo_prestamo.get()
    libros = obtener_libros()

    for libro in libros:
        if libro["codigo"] == codigo:
            if libro["disponible"]:
                messagebox.showwarning("Advertencia", "Este libro ya está disponible.")
            else:
                libro["disponible"] = True
                actualizar_estado(libro["codigo"], True)
                messagebox.showinfo("Devolución", "Libro devuelto con éxito.")
            e_codigo_prestamo.delete(0, tk.END)
            return

    # Si no se encontró ningún libro con ese código
    messagebox.showerror("Error", f"No se encontró ningún libro con el código: {codigo}")
    e_codigo_prestamo.delete(0, tk.END)

# Crear la ventana principal de la interfaz gráfica
root = tk.Tk()
root.title("Biblioteca funcional")

# Configuración de la de las cajas de texto y botones
tk.Label(root, text="Título").pack()
e_titulo = tk.Entry(root)
e_titulo.delete(0, tk.END)
e_titulo.pack()

tk.Label(root, text="Autor").pack()
e_autor = tk.Entry(root)
e_autor.delete(0, tk.END)
e_autor.pack()

tk.Label(root, text="Categoría").pack()
var_categoria = tk.StringVar(value="Ciencia")
tk.OptionMenu(root, var_categoria, "Ciencia", "Literatura", "Historia").pack()

tk.Label(root, text="Código").pack()
e_codigo = tk.Entry(root)
e_codigo.delete(0, tk.END)
e_codigo.pack()

tk.Button(root, text="Registrar libro", command=registrar).pack(pady=5)

tk.Label(root, text="Buscar por título o codigo").pack()
e_busqueda = tk.Entry(root)
e_busqueda.delete(0, tk.END)
e_busqueda.pack()
tk.Button(root, text="Consultar", command=consultar).pack()
tk.Button(root, text="Limpiar resultados", command=limpiar_resultado).pack(pady=5)

t_resultado = tk.Text(root, height=10, width=50)
t_resultado.delete("1.0", tk.END)
t_resultado.pack()

tk.Label(root, text="Código para préstamo/devolución").pack()
e_codigo_prestamo = tk.Entry(root)
e_codigo_prestamo.pack()
tk.Button(root, text="Prestar", command=prestar).pack()
tk.Button(root, text="Devolver", command=devolver).pack()

root.mainloop()
