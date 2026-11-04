from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = "esta_es_una_clave_secreta_muy_segura"
bcrypt = Bcrypt(app)

# Expresión regular para validar el formato del correo electrónico
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    is_valid = True
    
    # Validaciones de Registro
    if len(request.form['nombre']) < 2:
        flash("El nombre debe tener al menos 2 caracteres.", "register")
        is_valid = False
    elif not request.form['nombre'].isalpha():
        flash("El nombre solo debe contener letras.", "register")
        is_valid = False

    if len(request.form['apellido']) < 2:
        flash("El apellido debe tener al menos 2 caracteres.", "register")
        is_valid = False
    elif not request.form['apellido'].isalpha():
        flash("El apellido solo debe contener letras.", "register")
        is_valid = False

    if not EMAIL_REGEX.match(request.form['email']):
        flash("Formato de correo electrónico inválido.", "register")
        is_valid = False
    else:
        # Verificar si el correo ya existe en la base de datos
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        data = {"email": request.form['email']}
        user_in_db = connectToMySQL('usuarios_db').query_db(query, data)
        if user_in_db:
            flash("Este correo electrónico ya está registrado.", "register")
            is_valid = False

    if len(request.form['password']) < 8:
        flash("La contraseña debe tener al menos 8 caracteres.", "register")
        is_valid = False
    # (Opcional - Bonus Plata) Validar mayúscula y número:
    elif not re.search(r'[A-Z]', request.form['password']) or not re.search(r'[0-9]', request.form['password']):
        flash("La contraseña debe incluir al menos una mayúscula y un número.", "register")
        is_valid = False

    if request.form['password'] != request.form['confirm_password']:
        flash("Las contraseñas no coinciden.", "register")
        is_valid = False

    if not is_valid:
        return redirect('/')

    # Si todo es válido: hashear contraseña y guardar en la base de datos
    password_hash = bcrypt.generate_password_hash(request.form['password'])
    
    query = """INSERT INTO usuarios (nombre, apellido, email, password) 
               VALORES (%(nombre)s, %(apellido)s, %(email)s, %(password)s);""" # Nota: Asegúrate de usar VALUES en inglés si tu SQL da error
    
    # Corrección de la consulta con sintaxis SQL estándar de inserción:
    query = """INSERT INTO usuarios (nombre, apellido, email, password) 
               VALUES (%(_nombre)s, %(apellido)s, %(email)s, %(password)s);""" # Ajustado abajo limpio:
               
    query = """INSERT INTO usuarios (nombre, apellido, email, password) 
               VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s);"""
               
    data = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "password": password_hash
    }
    
    user_id = connectToMySQL('usuarios_db').query_db(query, data)
    
    # Guardar el ID del usuario en sesión
    session['user_id'] = user_id
    session['nombre'] = request.form['nombre']
    
    return redirect('/success')

@app.route('/login', methods=['POST'])
def login():
    # Buscar al usuario por correo electrónico
    query = "SELECT * FROM usuarios WHERE email = %(email)s;"
    data = {"email": request.form['email']}
    result = connectToMySQL('usuarios_db').query_db(query, data)
    
    if len(result) > 0:
        user = result[0]
        # Verificar la contraseña cifrada
        if bcrypt.check_password_hash(user['password'], request.form['password']):
            # Si coincide, guardamos los datos en sesión
            session['user_id'] = user['id']
            session['nombre'] = user['nombre']
            return redirect('/success')
            
    flash("Correo electrónico o contraseña inválidos.", "login")
    return redirect('/')

@app.route('/success')
def success():
    # Validar que el usuario haya iniciado sesión
    if 'user_id' not in session:
        flash("Debes iniciar sesión para acceder a esta página.", "login")
        return redirect('/')
        
    return render_template('success.html', nombre=session['nombre'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)