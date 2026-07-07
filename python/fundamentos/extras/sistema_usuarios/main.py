import sys
from usuario import Usuario

def menu_principal():
    while True:
        print("\n==============================")
        print("      SISTEMA DE USUARIOS")
        print("==============================")
        print("1. Iniciar sesión")
        print("2. Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            login()
        elif opcion == "2":
            print("¡Gracias por usar el sistema! Saliendo...")
            sys.exit()
        else:
            print("Opción inválida. Intente de nuevo.")

def login():
    print("\nInicio de Sesión")
    usuario_input = input("Usuario: ").strip()
    contrasena_input = input("Contraseña: ").strip()
    
    usuario_datos = Usuario.iniciar_sesion(usuario_input, contrasena_input)
    
    if usuario_datos:
        rol = usuario_datos['nombre_tipo']
        nombre = usuario_datos['nombre_usuario']
        
        if rol == 'ADMIN':
            menu_admin(nombre)
        elif rol == 'USER':
            menu_user(nombre)
    else:
        print("\nUsuario o contraseña incorrectos.")
        # Regresa automáticamente al menú inicial por el flujo del while anterior

def menu_admin(nombre_admin):
    while True:
        print("\n==============================")
        print(f"Bienvenido Administrador:\n{nombre_admin}")
        print("==============================")
        print("1. Registrar usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuario")
        print("4. Modificar usuario")
        print("5. Eliminar usuario")
        print("6. Cerrar sesión")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            ejecutar_registrar()
        elif opcion == "2":
            ejecutar_listar()
        elif opcion == "3":
            ejecutar_buscar()
        elif opcion == "4":
            ejecutar_modificar()
        elif opcion == "5":
            ejecutar_eliminar()
        elif opcion == "6":
            print("Cerrando sesión de Administrador...")
            break
        else:
            print("Opción inválida.")

def menu_user(nombre_usuario):
    while True:
        print("\n==============================")
        print("Bienvenido\n")
        print(nombre_usuario)
        print("\nTipo de usuario:\nUSER")
        print("==============================")
        print("1. Cerrar sesión")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            print("Cerrando sesión de Usuario...")
            break
        else:
            print("Opción inválida. Los usuarios estándar solo pueden cerrar sesión.")

# --- Funciones auxiliares para las acciones del Admin ---

def ejecutar_registrar():
    print("\n--- Registrar Usuario ---")
    username = input("Usuario: ").strip()
    contrasena = input("Contraseña: ").strip()
    tipo = input("Tipo (ADMIN o USER): ").strip().upper()
    
    if tipo not in ["ADMIN", "USER"]:
        print("Tipo de usuario no válido. Debe ser ADMIN o USER.")
        return

    # Mapeo según los IDs de tu tabla tipo_usuarios
    id_tipo = 1 if tipo == "ADMIN" else 2
    
    nuevo_usuario = Usuario(nombre_usuario=username, contrasena=contrasena, tipo_usuario=id_tipo)
    if nuevo_usuario.registrar_usuario():
        print("Usuario registrado con éxito.")
    else:
        print("No se pudo registrar el usuario (puede que ya exista el nombre de usuario).")

def ejecutar_listar():
    print("\n--- Listar Usuarios ---")
    lista = Usuario.listar_usuarios()
    if not lista:
        print("No hay usuarios registrados o disponibles.")
        return
    
    print(f"{'ID':<6} {'Usuario':<15} {'Tipo':<10}")
    print("-" * 35)
    for u in lista:
        print(f"{u['id_usuario']:<6} {u['nombre_usuario']:<15} {u['nombre_tipo']:<10}")

def ejecutar_buscar():
    print("\n--- Buscar Usuario ---")
    id_buscar = input("Ingrese el ID del usuario: ").strip()
    if not id_buscar.isdigit():
        print("El ID debe ser numérico.")
        return
        
    u = Usuario.buscar_usuario_por_id(int(id_buscar))
    if u:
        print("\nInformación del Usuario:")
        print(f"ID: {u['id_usuario']}")
        print(f"Usuario: {u['nombre_usuario']}")
        print(f"Contraseña: {u['contrasena']}")
        print(f"Tipo: {u['nombre_tipo']}")
    else:
        print("Usuario no encontrado.")

def ejecutar_modificar():
    print("\n--- Modificar Usuario ---")
    id_modificar = input("Ingrese el ID del usuario a modificar: ").strip()
    if not id_modificar.isdigit():
        print("El ID debe ser numérico.")
        return
    
    user_actual = Usuario.buscar_usuario_por_id(int(id_modificar))
    if not user_actual:
        print("Usuario no encontrado.")
        return
    
    print(f"Modificando datos actuales para el usuario: {user_actual['nombre_usuario']}")
    nuevo_username = input(f"Nuevo Usuario (Enter para mantener '{user_actual['nombre_usuario']}'): ").strip()
    nueva_contrasena = input(f"Nueva Contraseña (Enter para mantener '{user_actual['contrasena']}'): ").strip()
    nuevo_tipo = input(f"Nuevo Tipo ADMIN/USER (Enter para mantener '{user_actual['nombre_tipo']}'): ").strip().upper()
    
    # Si presionan enter se conservan los datos de la BD
    final_username = nuevo_username if nuevo_username else user_actual['nombre_usuario']
    final_contrasena = nueva_contrasena if nueva_contrasena else user_actual['contrasena']
    
    if nuevo_tipo:
        if nuevo_tipo not in ["ADMIN", "USER"]:
            print("Tipo inválido. No se realizaron cambios.")
            return
        final_id_tipo = 1 if nuevo_tipo == "ADMIN" else 2
    else:
        final_id_tipo = 1 if user_actual['nombre_tipo'] == "ADMIN" else 2
        
    usuario_actualizado = Usuario(
        id_usuario=int(id_modificar),
        nombre_usuario=final_username,
        contrasena=final_contrasena,
        tipo_usuario=final_id_tipo
    )
    
    if usuario_actualizado.modificar_usuario():
        print("Usuario actualizado con éxito.")
    else:
        print("Hubo un error al intentar actualizar.")

def ejecutar_eliminar():
    print("\n--- Eliminar Usuario ---")
    id_eliminar = input("Ingrese el ID del usuario a eliminar: ").strip()
    if not id_eliminar.isdigit():
        print("El ID debe ser numérico.")
        return
        
    if Usuario.eliminar_usuario(int(id_eliminar)):
        print("Usuario eliminado exitosamente.")
    else:
        print("No se pudo eliminar el usuario.")

if __name__ == "__main__":
    menu_principal()