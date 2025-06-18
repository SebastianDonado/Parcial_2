def crear_libro(titulo, autor, categoria, codigo):  #Creamos una función para crear un libro
    return {
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "codigo": codigo,
        "disponible": True
    }

def buscar_libros(libros, consulta):
    consulta = consulta.lower()    #utilizo lower() para que la búsqueda no sea sensible a mayúsculas y minúsculas
    # # filtro los libros que coincidan con el título o el codigo, es util para realizaar otros procesos
    return list(filter(lambda l: consulta in l["titulo"].lower() or consulta in l["codigo"].lower(), libros))   
#con las siguietes funciones se marca el estado del libro
#imporante decir que lamda se utilia como una funcion simple para modificar el estado del libro,
def marcar_prestamo(libros, codigo):
    return list(map(lambda l: {**l, "disponible": False} if l["codigo"] == codigo else l, libros)) 

def marcar_devolucion(libros, codigo):
    return list(map(lambda l: {**l, "disponible": True} if l["codigo"] == codigo else l, libros))
