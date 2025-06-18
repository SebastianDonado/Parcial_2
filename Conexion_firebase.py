import firebase_admin
from firebase_admin import credentials, db, firestore

cred = credentials.Certificate("base_de_datos.json")
#firebase_admin.initialize_app(cred,{"databaseURL" : "https://parcial-biblioteca-default-rtdb.firebaseio.com/"
#})
firebase_admin.initialize_app(cred)
db = firestore.client()
# Con esta funcion se guarda el libro en la base de datos y se convierte un diccionario a un documento de Firestore
def guardar_libro(libro):
    db.collection("libros").document(libro["codigo"]).set(libro)
# Esta funcion obtiene todos los libros de la base de datos y los devuelve como una lista de diccionarios
def obtener_libros():
    docs = db.collection("libros").stream()
    return [doc.to_dict() for doc in docs]
# Esta funcion actualiza el estado de un libro (disponible o no) en la base de datos
def actualizar_estado(codigo, disponible):
    db.collection("libros").document(codigo).update({"disponible": disponible})


