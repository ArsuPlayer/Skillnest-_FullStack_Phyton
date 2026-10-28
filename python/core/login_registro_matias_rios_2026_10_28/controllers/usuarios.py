from flask import render_template, redirect, request, session, flash
from server import app
from models.usuarios import Usuario

@app.route('/')
def index():
    if 'usuario_id' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not Usuario.validar_registro(request.form):
        return redirect('/')
    # Resto de tu código de registro...
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    # Tu código de login...
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        return redirect('/logout')
    usuario = Usuario.get_by_id({'id': session['usuario_id']})
    return render_template('dashboard.html', usuario=usuario)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')