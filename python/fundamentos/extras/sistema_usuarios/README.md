# Sistema de Gestión de Usuarios (CRUD + MySQL)

Este es un sistema de consola interactivo desarrollado en **Python** utilizando el paradigma de **Programación Orientada a Objetos (POO)**. El sistema se conecta a una base de datos relacional **MySQL** a través de la librería `pymysql` y permite gestionar usuarios mediante un CRUD completo, diferenciando los accesos y permisos por roles (`ADMIN` y `USER`).

---

## 📂 Estructura del Proyecto

El proyecto está organizado de la siguiente manera para mantener un código limpio y modular:

```text
sistema_usuarios/
├── conexion.py      # Gestiona la conexión y desconexión a la base de datos MySQL.
├── usuario.py       # Modelo y lógica de negocio. Contiene el CRUD y consultas SQL.
├── main.py          # Punto de entrada del programa. Controla los menús con ciclos `while`.
└── README.md        # Documentación del proyecto.