from flask import Flask, render_template, request
import pyodbc
import platform

app = Flask(__name__)

# 🔍 Detectar entorno y elegir driver correcto
if platform.system() == 'Linux':
    DRIVER_NAME = '{ODBC Driver 18 for SQL Server}'
    ENCRYPT = 'Encrypt=no;'
else:
    DRIVER_NAME = '{ODBC Driver 17 for SQL Server}'  # o el que tengas en tu PC
    ENCRYPT = ''  # en Windows local no hace falta

# 🔧 Conexión SQL Server compatible con Windows y Render
conexion = pyodbc.connect(
    f'DRIVER={DRIVER_NAME};'
    'SERVER=26.95.196.200;'
    'DATABASE=CASTILLONV2;'
    'UID=sa;'
    'PWD=Castillon1234+;'
    f'{ENCRYPT}'
)

@app.route('/', methods=['GET', 'POST'])
def login():
    mensaje = ""
    productos = []

    if request.method == 'POST':
        usuario = request.form['usuario'].strip()
        clave = request.form['clave'].strip()

        cursor = conexion.cursor()
        query = """
            SELECT COUNT(*) 
            FROM USUARIO 
            WHERE LOGEO COLLATE Latin1_General_CI_AI = ? 
              AND CLAVE = ? 
              AND ESTADO = 1
        """
        cursor.execute(query, (usuario, clave))
        resultado = cursor.fetchone()[0]

        if resultado == 1:
            cursor.execute("SELECT NOMPRODUCTO, DESCRIPCION, PRECIO, MARCA FROM PRODUCTO WHERE ESTADO = 1")
            productos = cursor.fetchall()
        else:
            mensaje = "❌ Credenciales incorrectas o usuario inactivo."

    return render_template("login.html", mensaje=mensaje, productos=productos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
