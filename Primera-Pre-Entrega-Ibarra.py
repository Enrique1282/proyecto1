def crear_cuenta():
    
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    # Abrir el archivo en modo escritura para cargando los datos
    with open("MiRegistro.txt", "a") as archivo:
        archivo.write(f"{usuario},{contraseña}\n")
    
    print("Cuenta creada exitosamente!")

def iniciar_sesion():

    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    #Abrir el archivo en modo lectura para ver si coinsiden
    with open("MiRegistro.txt", "r") as archivo:
        for linea in archivo:
            MiRegistro = linea.strip().split(",")
            if usuario == MiRegistro[0] and contraseña == MiRegistro[1]:
                print("Inicio de sesión exitoso!")
                return

    print("Nombre de usuario o contraseña incorrectos.")
   
# abrir menu
while True:
    print("1. Crear cuenta")
    print("2. Iniciar sesión")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_cuenta()
    elif opcion == "2":
        iniciar_sesion()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")