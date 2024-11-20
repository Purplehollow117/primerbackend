from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Asegúrate de tener un archivo 'datos.txt' en tu directorio de trabajo
file_path = 'datos.txt'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Html1')
def html1():
    return render_template('Html1/index.html')

@app.route('/Html2')
def html2():
    return render_template('Html2/index.html')

@app.route('/powerpoint')
def powerpoint():
    return render_template('powerpoint/pp.html')

@app.route('/Juego/Hangman')
def hangman():
    return render_template('Juego/Hangman.html')

# Ruta para manejar el envío del formulario
@app.route('/submit', methods=['POST'])
def submit():
    # Datos del formulario
    nombre = request.form['nombre']
    correo = request.form['correo']
    mensaje = request.form['mensaje']
    
    # Guardar los datos en datos.txt
    with open(file_path, 'a') as file:
        file.write(f'Nombre: {nombre}\nCorreo: {correo}\nMensaje: {mensaje}\n\n')
    
    return "Datos enviados correctamente!"

if __name__ == '__main__':
    # Crear el archivo si no existe
    if not os.path.exists(file_path):
        with open(file_path, 'w'): pass
    
    app.run(debug=True)
