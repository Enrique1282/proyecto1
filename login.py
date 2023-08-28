def iniciar_sesion():
    # Solicitar al usuario el nombre de usuario y la contraseña para iniciar sesión
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    # Abrir el archivo en modo de lectura y comprobar si las credenciales son correctas
    with open("basededatos.txt", "r") as archivo:
        for linea in archivo:
            credenciales = linea.strip().split(",")
            if usuario == credenciales[0] and contraseña == credenciales[1]:
                print("Inicio de sesión exitoso!")
                return

    print("Nombre de usuario o contraseña incorrectos.")

# Menú principal
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