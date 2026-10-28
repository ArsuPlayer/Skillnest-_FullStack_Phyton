from config.mysqlconnection import connectToMySQL
from flask import flash
import re
from datetime import datetime, date

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NOMBRE_REGEX = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*\d).+$')
class Usuario:
    DB = "bd_login_registro"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.fecha_nacimiento = data.get('fecha_nacimiento')
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO usuarios (first_name, last_name, email, password, fecha_nacimiento)
            VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(fecha_nacimiento)s);
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validar_registro(formulario):
        is_valid = True

        # Validar Nombre
        if len(formulario['first_name']) < 2 or not NOMBRE_REGEX.match(formulario['first_name']):
            flash("El nombre debe contener solo letras y tener al menos 2 caracteres.", "register")
            is_valid = False

        # Validar Apellido
        if len(formulario['last_name']) < 2 or not NOMBRE_REGEX.match(formulario['last_name']):
            flash("El apellido debe contener solo letras y tener al menos 2 caracteres.", "register")
            is_valid = False

        # Validar Email
        if not EMAIL_REGEX.match(formulario['email']):
            flash("Formato de correo electrónico inválido.", "register")
            is_valid = False
        else:
            usuario_existente = Usuario.get_by_email({'email': formulario['email']})
            if usuario_existente:
                flash("El correo electrónico ya está registrado.", "register")
                is_valid = False

        if not formulario.get('fecha_nacimiento'):
            flash("Debes ingresar tu fecha de nacimiento.", "register")
            is_valid = False
        else:
            fecha_nac = datetime.strptime(formulario['fecha_nacimiento'], '%Y-%m-%d').date()
            hoy = date.today()
            edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
            if edad < 18:
                flash("Debes ser mayor de 18 años para registrarte.", "register")
                is_valid = False

        if len(formulario['password']) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", "register")
            is_valid = False

        if not PASSWORD_REGEX.match(formulario['password']):
            flash("La contraseña debe contener al menos un número y una letra mayúscula.", "register")
            is_valid = False

        if formulario['password'] != formulario['confirm_password']:
            flash("Las contraseñas no coinciden.", "register")
            is_valid = False

        return is_valid