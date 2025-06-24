from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render libera uma porta dinâmica
    app.run(host='0.0.0.0', port=port)
