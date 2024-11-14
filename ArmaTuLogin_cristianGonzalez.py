from os import system


def nuevo_usuario(): #Funcion para registrar un nuevo usuario
    nombre = input("Nombre: ")
    while True:
        contra = input("Contraseña(mayor a 4 caracteres): ")
        if len(contra)<=4:
            print("La contraseña debe ser mas larga.")
        else:
            break
    
    if nombre in usuarios:
        print("Usuario existente.")
    else:
        usuarios[nombre]={
            "contraseña":contra
        }
        print("Usuario agregado con exito, presiobe ENTER para continuar.")
        enter = input("")
        system("cls")


def listar_usuarios(): #Funcion para listar todos los usuarios, solo los nombres, no las contraseñas
    for nombre in usuarios:
        print(nombre)
    enter = input("Presione ENTER para continuar.")
    system("cls")
    
def logueo(): #Funcion para iniciar sesion solicitando nombre y contraseña 
    usuario_login = input("Nombre: ")
    if usuario_login in usuarios:
        for intento in range (2,-1,-1):   
            contraseña_loguin=input("Contraseña: ")
            if usuarios[usuario_login]["contraseña"] == contraseña_loguin:
                print("Inicio de sesión exitoso!!!")
                enter = input("")
                system("cls")
                break
            else:
                print("Contraseña incorrecta, quedan " + str(intento) + " intentos.")
    else:
        print("Usuario no registrado.")
        enter = input("")
        system("cls")

def modificar_contra(): #Funcion para modificar la contraseña de un usuario previamente registrado
    nombre_mod=input("Nombre de usuario a modificar: ")
    if nombre_mod in usuarios:
        contra_modificar=input("Contraseña del usuario: ")
        if usuarios[nombre_mod]["contraseña"] == contra_modificar:
            nueva_contra=input("Nueva contraseña: ")
            usuarios[nombre_mod]["contraseña"] = nueva_contra 
            print("Usuario modificado con éxito.")
            enter = input("")
            system("cls")
    else:
        print("Usuario inexistente.")
        enter = input("")
        system("cls")

def eliminar_usuario(): #Funcion para eliminar usuarios existentes
    usuario_eliminar = input("Nombre de usuario a eliminar: ")
    if usuario_eliminar in usuarios:
        confirmacion = input(f"¿Estás seguro de eliminar el usuario '{usuario_eliminar}'?(s/n)").lower()
        if confirmacion == "s":
            usuarios.pop(usuario_eliminar)
            print("Usuario eliminado con exito!")
        elif confirmacion == "n":
            print("Eliminacion cancelada.")
        else:
            print("El valor ingresado no es correcto.")
    else:
        print("Usuario no encontrado.")
    enter = input("")
    system("cls")
    
def mostrar_titulo(): #Funcion para mostrar titulo del programa
            print("""
    ==============================================
        Gestor de usuarios - Cristian Gonzalez
    ==============================================
    """)
        
        
        
usuarios={}

"""
Try Except utilizado para evitar mostrar errores cuando se corta el programa manualmente.
"""

try:
    while True: #Flujo principal del programa
        system("cls")
        mostrar_titulo()
        print("1. Registro")
        print("2. Listar usuarios")
        print("3. Login")
        print("4. Cambiar contraseña")
        print("5. Eliminar usuario")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nuevo_usuario()
        elif opcion == '2':
            listar_usuarios()
        elif opcion == '3':
            logueo()
        elif opcion == '4':
            modificar_contra()
        elif opcion == "5":
            eliminar_usuario()
        elif opcion == '0':
            print("Adios...")
            break
        else:
            print("El caracter ingresado no es valido, intente de nuevo.")
            enter = input("")
            system("cls")
except:
    print("\n\nSe interrumpio la ejecucion del programa...")
   
        
            
