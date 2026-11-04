from usuario import Usuario

def menu_admin(usuario_sesion):
    """Menú interactivo exclusivo para administradores."""
    while True:
        print("\n==============================")
        print(f"Bienvenido Administrador:\n{usuario_sesion.usuario}")
        print("==============================")
        print("1. Registrar usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuario")
        print("4. Modificar usuario")
        print("5. Eliminar usuario")
        print("6. Cerrar sesión")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n--- Registrar Nuevo Usuario ---")
            nuevo_user = input("Usuario: ").strip()
            nueva_pass = input("Contraseña: ").strip()
            nuevo_tipo = input("Tipo (ADMIN / USER): ").strip().upper()
            
            if nuevo_tipo not in ["ADMIN", "USER"]:
                print("Tipo inválido. Debe ser ADMIN o USER.")
                continue

            instancia = Usuario()
            if instancia.crear_usuario(nuevo_user, nueva_pass, nuevo_tipo):
                print("¡Usuario registrado exitosamente!")
            else:
                print("No se pudo registrar el usuario.")

        elif opcion == "2":
            print("\n--- Listado de Usuarios ---")
            usuarios = Usuario.obtener_listado()
            if usuarios:
                print(f"{'ID':<5} {'Usuario':<15} {'Tipo':<10}")
                print("-" * 35)
                for u in usuarios:
                    print(f"{u['id']:<5} {u['usuario']:<15} {u['tipo']:<10}")
            else:
                print("No hay usuarios registrados.")

        elif opcion == "3":
            print("\n--- Buscar Usuario por ID ---")
            try:
                id_buscado = int(input("Ingrese el ID del usuario: "))
                u = Usuario.buscar_por_id(id_buscado)
                if u:
                    print(f"\nID: {u['id']}")
                    print(f"Usuario: {u['usuario']}")
                    print(f"Tipo: {u['tipo']}")
                    print(f"Creado: {u['created_at']}")
                else:
                    print("Usuario no encontrado.")
            except ValueError:
                print("Por favor, ingrese un ID numérico válido.")

        elif opcion == "4":
            print("\n--- Modificar Usuario ---")
            try:
                id_mod = int(input("Ingrese el ID del usuario a modificar: "))
                u_actual = Usuario.buscar_por_id(id_mod)
                if not u_actual:
                    print("Usuario no encontrado.")
                    continue
                
                print(f"Modificando a: {u_actual['usuario']} ({u_actual['tipo']})")
                nuevo_user = input(f"Nuevo usuario [{u_actual['usuario']}]: ").strip() or u_actual['usuario']
                nueva_pass = input("Nueva contraseña: ").strip() or u_actual['password']
                nuevo_tipo = input(f"Nuevo tipo (ADMIN/USER) [{u_actual['tipo']}]: ").strip().upper() or u_actual['tipo']

                instancia = Usuario()
                if instancia.modificar_usuario(id_mod, nuevo_user, nueva_pass, nuevo_tipo):
                    print("¡Usuario modificado exitosamente!")
                else:
                    print("No se pudo modificar el usuario.")
            except ValueError:
                print("Por favor, ingrese un ID numérico válido.")

        elif opcion == "5":
            print("\n--- Eliminar Usuario ---")
            try:
                id_elim = int(input("Ingrese el ID del usuario a eliminar: "))
                u_actual = Usuario.buscar_por_id(id_elim)
                if not u_actual:
                    print("Usuario no encontrado.")
                    continue

                confirmar = input(f"¿Está seguro de eliminar al usuario '{u_actual['usuario']}'? (s/n): ").strip().lower()
                if confirmar == 's':
                    if Usuario.eliminar_usuario(id_elim):
                        print("¡Usuario eliminado exitosamente!")
                    else:
                        print("No se pudo eliminar el usuario.")
                else:
                    print("Operación cancelada.")
            except ValueError:
                print("Por favor, ingrese un ID numérico válido.")

        elif opcion == "6":
            print("\nCerrando sesión de administrador...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def menu_user(usuario_sesion):
    """Menú interactivo para usuarios comunes (USER)."""
    while True:
        print("\n==============================")
        print("Bienvenido")
        print(f"\n{usuario_sesion.usuario}")
        print("\nTipo de usuario:")
        print("USER")
        print("==============================")
        print("1. Cerrar sesión")
        
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            print("\nCerrando sesión...")
            break
        else:
            print("Opción inválida.")

def main():
    """Función principal que controla el flujo de inicio de sesión."""
    while True:
        print("\n==============================")
        print("      SISTEMA DE USUARIOS     ")
        print("==============================")
        print("1. Iniciar sesión")
        print("2. Salir")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n--- Inicio de Sesión ---")
            user_input = input("Usuario: ").strip()
            pass_input = input("Contraseña: ").strip()

            usuario_obj = Usuario()
            usuario_autenticado = usuario_obj.validar_inicio_sesion(user_input, pass_input)

            if usuario_autenticado:
                print(f"\n¡Inicio de sesión exitoso! Rol: {usuario_autenticado.tipo}")
                if usuario_autenticado.tipo == "ADMIN":
                    menu_admin(usuario_autenticado)
                elif usuario_autenticado.tipo == "USER":
                    menu_user(usuario_autenticado)
            else:
                print("\nUsuario o contraseña incorrectos.")
        elif opcion == "2":
            print("\nSaliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("\nOpción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()