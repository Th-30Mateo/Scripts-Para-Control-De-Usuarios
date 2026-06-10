import random

usuarios = []

rolesUser = ("admin", "user")

userID = 0

def crear_usuario():
    print("")

    print("Vamos a generar tu usuario. Te pedire algunos datos.")
    print("")
   

    while True:

        nombre = input("Ingrese su nombre: ").strip()
        print("")

        if not nombre.isalpha():

            print("Nombre invalido, ingrese otra vez.")
            print("")
        else:

            break
        
    while True:

        apellido = input("Ingrese su apellido: ").strip()
        print("")

        if not apellido.isalpha():

            print("Apellido invalido, ingrese otra vez.")
            print("")
        else:

            break

    while True:

        edad = input("Ingrese su edad: ")

        if not edad.isdigit():
            print("")
            print("Ingrese un numero, no letras.")
        else:

            edad = int(edad)

            if edad >= 105 or edad <= 0:
                print("")

                print("Edad invalida, ingrese otra vez.")
            else:

                break

    while True:
        print("")

        print("Ingrese su rol, admin o user")
        print("")
        rol = input("¿Que rol ocupa? ").strip().lower()

        if rol not in rolesUser:
            print("")

            print("Rol no permitido. Ingrese un rol valido!!")
        else:

            break

    generador_usuario = nombre.lower() + "." +  apellido.lower()

    for u in usuarios:

        if u["usuario"] == generador_usuario:
            print("")

            print("Ese usuario ya existe!! Cree otro.")
            return

    global userID

    userID +=1

    usuario = {

            "ID" : userID,

            "nombre": nombre,

            "apellido": apellido,

            "usuario":generador_usuario,

            "edad": edad,
            "rol": rol

    }

    usuarios.append(usuario)

    print("Usuario creado correctamente!!")
    print("")

    print(f"Datos: ID: {usuario['ID']}, Nombre: {usuario['nombre']} {usuario['apellido']}, Usuario: {usuario['usuario']}, Edad: {usuario['edad']}, Rol: {usuario['rol']}\n")
    

def lista_usuarios():

    if len(usuarios) == 0:

        print("No hay usuarios registrados.")
        return

    for usuario in usuarios:
        print("")

        print(f"ID: {usuario['ID']}")
        print("")

        print(f"Usuario: {usuario['usuario']}")
        print("")

        print(f"Nombre: {usuario['nombre']}")
        print("")

        print(f"Apellido: {usuario['apellido']}")
        print("")

        print(f"Rol: {usuario['rol']}")

def buscar_usuario():

    while True:

        print("Quiere buscar usuario por nombre o ID")

        print("-1- para buscar por USUARIO")

        print("-2- para buscar por ID")

        print("-3- para volver al menú principal")

        opcion = input("Ingrese opcion. ").strip().lower()

        if opcion == "3":

            break

        match opcion:

            case "1":
                print("")

                buscarXusuario = input("Ingrese su usuario con formato 'nombre.apellido':  ")

                for usuario in usuarios:

                    if usuario["usuario"] == buscarXusuario:

                        print(f"ID: {usuario['ID']}")

                        print(f"Usuario: {usuario['usuario']}")

                        print(f"Nombre: {usuario['nombre']}")

                        print(f"Apellido: {usuario['apellido']}")

                        print(f"Rol: {usuario['rol']}")
                        return
                    

                print("Usuario no encontrado.")

            case "2":

                buscarXid = int(input("Ingrese su N° de ID correspondiente a su usuario:  "))

                for usuario in usuarios:

                    if usuario["ID"] == buscarXid:

                        print(f"ID: {usuario['ID']}")

                        print(f"Usuario: {usuario['usuario']}")

                        print(f"Nombre: {usuario['nombre']}")

                        print(f"Apellido: {usuario['apellido']}")

                        print(f"Rol: {usuario['rol']}")
                        return

            case _:

                print("Opcion invalida!!")
                continue

def editar_usuario():

    userEdit = int(input("Ingresar ID para buscar su usuario: "))


    for usuario in usuarios:

        if userEdit == usuario["ID"]:

            while True:

                print("Ingrese 1 para editar NOMBRE.")

                print("Ingrese 2 para editar APELLIDO.")

                print("Ingrese 3 para editar EDAD.")

                print("Ingrese 4 para editar ROL.")

                print("Ingrese 0 para salir.")

                opcion = input("Seleccione una opcion: ")

                if opcion == "0":

                    break
                    return

                elif opcion== "1":

                    nuevoNombre = input("Ingrese nombre: ").lower().strip()

                    usuario["nombre"] = nuevoNombre
                    print(f"Nombre actualizado!! Nuevo nombre: {nuevoNombre}")
                    usuario["usuario"] = nuevoNombre.lower() + "." + usuario["apellido"].lower()

                elif opcion == "2":

                    nuevoApellido = input("Ingrese apellido: ").lower().strip()

                    usuario["apellido"] = nuevoApellido
                    print(f"Apellido actualizado!! Nuevo apellido: {nuevoApellido}")
                    usuario["usuario"] = usuario["nombre"].lower() + "." + nuevoApellido.lower()
                elif opcion == "3":

                    nuevaEdad = input("Ingrese su edad: ")

                    if nuevaEdad.isdigit():

                        nuevaEdad = int(nuevaEdad)

                        if 1 <= nuevaEdad <= 105:

                            usuario["edad"] = nuevaEdad
                            print(f"Edad actualizada!! Nueva edad: {nuevaEdad}")
                        else:

                            print("Edad fuera de rango (1-105)")
                    else:

                        print("Debe ingresar un número: ")

                    usuario["edad"] = nuevaEdad

                elif opcion == "4":

                    nuevoRol = input("Ingrese nuevo Rol: ")

                    usuario["rol"] = nuevoRol
                    print(f"Rol actualizado!! Nuevo rol: {nuevoRol}")
                else:

                    print("Opcion Invalida!!")
                    continue

def eliminar_usuario():

    try:

        id_eliminar = int(input("ID del usuario a eliminar: "))         

    except ValueError:

        print("ID invalido. Debe ser un numero.")
        return

    for indice, usuario in enumerate(usuarios):

        if usuario["ID"] == id_eliminar:

            confirmacion = input(f"¿Confirma que desea eliminar al usuario {usuario['usuario']}? (s/n): ").strip().lower()

            if confirmacion == "s":

                usuarios.pop(indice)

                print("Usuario eliminado correctamente.")
            else:
                print("operacion cancelada")
            return

    print("Usuario no encontrado.")

def generar_usuario_al_azar():
    nombres = ["Juan", "Maria", "Carlos", "Ana", "Luis", "Sofia", "Pedro", "Lucia", "Diego", "Valentina"]
    apellidos = ["Gomez", "Perez", "Rodriguez", "Garcia", "Lopez", "Martinez", "Sanchez", "Diaz", "Fernandez", "Torres"]
    roles = ("user",)
    global userID
    userID += 1
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    edad = random.randint(1, 105)
    rol = random.choice(roles)
    generador_usuario = nombre.lower() + "." +  apellido.lower()
    for u in usuarios:
        if u["usuario"] == generador_usuario:
            print("")
            print("Ese usuario ya existe!! Cree otro.")
            return

    usuario = {
            "ID" : userID,
            "nombre": nombre,       
            "apellido": apellido,
            "usuario":generador_usuario,
            "edad": edad,
            "rol": rol
    }
    usuarios.append(usuario)
    print("")
    print("Usuario generado correctamente!!")
    print("")
    print(f"Datos: ID: {usuario['ID']}, Nombre: {usuario['nombre']} {usuario['apellido']}, Usuario: {usuario['usuario']}, Edad: {usuario['edad']}, Rol: {usuario['rol']}\n")


def mostrar_usuarios():
    total_usuarios = len(usuarios)
    print("")
    print(f"Cantidad total de usuarios: {total_usuarios}")
    print("")
    if total_usuarios > 0:
        cantidad_admins = 0
        cantidad_users = 0
        for u in usuarios:
            if u["rol"] == "admin":
                cantidad_admins += 1
            elif u["rol"] == "user":
                cantidad_users += 1
    
    print(f"Cantidad de admins: {cantidad_admins}")
    print("")
    print(f"Cantidad de users: {cantidad_users}")
    print("")

def mostrar_user_aleatorio():
    userAleatorio = random.choice(usuarios)
    print("")
    print("")


    print("----El usuario aleatorio encontrado es-----")

    print("")
    print("")

    print(f"USUARIO ALEATORIO: ID: {userAleatorio['ID']}")
    print("")
    print(f"Usuario: {userAleatorio['usuario']}")
    print("")
    print(f"Nombre: {userAleatorio['nombre']}")
    print("")
    print(f"Apellido: {userAleatorio['apellido']}")
    print("")
    print(f"Edad: {userAleatorio['edad']}")
    print("")
    print(f"Rol: {userAleatorio['rol']}")
    print("")
    print("")

while True:
    print("")

    print("1.Crear usuario")
    print("")
    print("2.Lista de usuarios")
    print("")
    print("3.Buscar usuario")
    print("")
    print("4.Editar usuario")
    print("")
    print("5.Eliminar usuario")
    print("")
    print("6.Generar usuario")
    print("")
    print("7.Mostrar cantidad usuarios")
    print("")
    print("8.Mostrar usuario aleatorio")
    print("")
    print("0.Salir")
    print("")
            
            

    opcion = input("Seleccione una opcion:   ")


    match opcion:

        case "1":

            crear_usuario()

        case "2":

            lista_usuarios()
        case "3":
            buscar_usuario()
        case "4":
            editar_usuario()
        case "5":
            eliminar_usuario()
        case "6":
            generar_usuario_al_azar()
        case "7":
            mostrar_usuarios()
        case "8":
            mostrar_user_aleatorio()
        case "0":

            print("Saliendo... ")
            print("//Grupo -10-//")

            break

        case _:

            print("opcion incorrecta. Ingrese una opcion valida")
            continue