# Sistema de Gestión de Usuarios con Inicio de Sesión // Matías Ríos

Aplicación de consola desarrollada en Python aplicando Programación Orientada a Objetos (POO) y PyMySQL, diseñada para administrar accesos mediante control de roles (Administrador y Usuario Común).

## Tecnologías Utilizadas
- Python 3
- MySQL
- PyMySQL (Librería de conexión)
- Programación Orientada a Objetos (POO)

## Instrucciones de Instalación y Ejecución
1. Configura la base de datos ejecutando el script `resources/crear_bd.sql` en tu servidor MySQL local.
2. Carga los datos iniciales ejecutando el script `resources/poblar_datos.sql`.
3. Instala la dependencia PyMySQL en tu entorno:
   ```bash
   pip install pymysql