# Parcial_2
Encontraremos el código comentado y una breve explicación del mismo

### ESTRUCTURA
La estructura esta conformada por tres archivos, uno donde se inializa firebase, el otro donde se encuebtra la extencion de las funciones y el ultimo donde trabajamos la interfaz gráfica.


####CONFIGURACION FIREBASE
En este encontraos la inicialización del firabase donde se inicializa con el archivo json o clave unica que nos ofrece la pagina y la trabajamos co firestore:

![image](https://github.com/user-attachments/assets/d027e1d6-e803-4adb-8738-4fb2d2bd56a8)

En la imagen encontramos la explicación de cada función pero en pocas palabras lo que tenemos aqui es un CRUD, para subir libros a la base de datos, traer los que ya estan allí para realizar busquedas ya sea para saber si esta disponible o no, o simplemente el libro no se encuentra en la bilioteca y por ultimo una actualizació de datos para cambiar de estado el libro etre prestado y disponile.


####FUNIONES
Aquí encontramos acciones mas especificas que conmbinaremos con lo que ya creamos en el archivo anterior, claramente esto se hara en la interfaz gráfia:

![image](https://github.com/user-attachments/assets/8e0aeb50-1d2f-47bb-8582-ec77254bbf1b)

Nuevamente el código se encuetra muy bien comentado, pero también te cuento en resumidas cuentas lo que tenemos aquí: en la función crear_libro estamos creando un diccionario con los campos suficinetes para registrarlo, en busqueda_libros tenemos una consulta que la hacemos que no sea sencible a mayusculas y minusculas con lower() y realizamos también un for para realizar dicha busqueda y por ultimo creamos dos funciones que realizan un proseso de marcaje entre prestado o disponible.

####INTERFAZ GRÁFICA
Primero importamos lo necesario

![image](https://github.com/user-attachments/assets/20881190-b9bc-40b0-a9e0-0704b10d731f)

Luego creamos las funciones necesarias:

![image](https://github.com/user-attachments/assets/35ccc14e-faf5-4131-98bb-22adf9673a78)

![image](https://github.com/user-attachments/assets/9549ef2e-3049-4013-9a46-09a42b92de49)

![image](https://github.com/user-attachments/assets/43088385-94a8-45c7-b314-44d656880872)

Ahora creamos la ventana, los label que nos ayudaran mediante un entry a crear cajas de texto, los botones que serviran para realizar acciones y cajas de texto que nos permitiran mostrar mensajes:

![image](https://github.com/user-attachments/assets/0d7106cb-ef43-41d4-a38c-190bdb0843f9)

![image](https://github.com/user-attachments/assets/9d9b5b63-00f7-4648-b486-d781b4457991)


####  Ejecución
######Cuando registro

![image](https://github.com/user-attachments/assets/0d760ad7-8f22-4b9d-8496-17d43da0d07c)

######Cuando realizo una busqueda

![image](https://github.com/user-attachments/assets/50b0b96e-f7ce-4103-ab87-04c692e0615c)

cuando esta mal

![image](https://github.com/user-attachments/assets/7a031ad1-84df-40c5-b027-0fe38e6606ab

######Cuando realizo pestamo y devolucion

![image](https://github.com/user-attachments/assets/405b7a8c-1b60-4303-a90a-e0fb1baf5d87)

![image](https://github.com/user-attachments/assets/dc8859fe-5bf8-4f0f-8112-796da9f7ab2c)












