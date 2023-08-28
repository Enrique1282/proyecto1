import sqlite3


def registro():
    # Abrir la conexión a la base de datos
    conexion = sqlite3.connect("BaseDeDatos.db")
    cursor = conexion.cursor()
    
    # Solicitar al usuario que ingrese los datos requeridos
    usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if len(contraseña) < 3:
        print("La contraseña debe tener al menos 3 caracteres.")
        conexion.close()
        return
    
    # Insertar un registro en la tabla.
    cursor.execute("INSERT INTO usuarios VALUES (?, ?)", (usuario, contraseña))
    
    # Guardar los datos en la base de datos.
    conexion.commit()
    
    # Cerrar la conexión con la base de datos.
    conexion.close()
    
    print("Registro exitoso. Bienvenido,", usuario)



def leerData():
    # Abrir la conexión a la base de datos
    conexion = sqlite3.connect("BaseDeDatos.db")
    cursor = conexion.cursor()
    
    # Obtener todos los registros de la tabla usuarios
    cursor.execute("SELECT * FROM usuarios")
    registros = cursor.fetchall()
    
    # Verificar si hay registros antes de imprimirlos
    if registros:
        # Imprimir los registros
        for registro in registros:
            print(registro)
    else:
        print("No hay registros en la base de datos.")
    
    # Cerrar la conexión con la base de datos.
    conexion.close()


def guardar_basededatos():
    # Abrir la conexión a la base de datos
    conexion = sqlite3.connect("BaseDeDatos.db")
    cursor = conexion.cursor()
    
    # Obtener todos los registros de la tabla usuarios
    cursor.execute("SELECT * FROM usuarios")
    registros = cursor.fetchall()
    
    # Verificar si hay registros antes de guardarlos en el archivo
    if registros:
        # Crear un archivo .txt
        archivo = open("basededatos.txt", "w")
        
        # Guardar los registros en el archivo .txt
        for registro in registros:
            linea = f"{registro[0]}\t{registro[1]}\n"  # Suponiendo que la tabla tiene 2 columnas: usuario y contraseña
            archivo.write(linea)
        
        # Cerrar el archivo.
        archivo.close()
    else:
        print("No hay registros en la base de datos.")
    
    # Cerrar la conexión con la base de datos.
    conexion.close()

def login():
    # Abrir la conexión a la base de datos
    conexion = sqlite3.connect("BaseDeDatos.db")
    cursor = conexion.cursor()
    
    # Solicitar al usuario que ingrese nombre de usuario y contraseña
    usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    
    # Obtener el registro correspondiente al nombre de usuario ingresado
    cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (usuario,))
    registro = cursor.fetchone()
    
    # Verificar si el registro existe y si la contraseña coincide
    if registro and registro[1] == contraseña:
        print("Login exitoso. Bienvenido,", usuario)
        # Aquí puedes continuar con el resto del programa
    else:
        print("Nombre de usuario o contraseña incorrectos.")
        # Aquí puedes dar al usuario la opción de volver a intentarlo o salir del programa
    
    # Cerrar la conexión con la base de datos.
    conexion.close()




if __name__ == '__main__':
    # Llamar a la función de registro para agregar un nuevo usuario
    registro()
    
    # Llamar a la función de login para probar el inicio de sesión
    login()
    
    # Llamar a la función de leerData para mostrar los registros en la base de datos
    leerData()
    
    # Llamar a la función para guardar la base de datos en el archivo .txt
    guardar_basededatos()