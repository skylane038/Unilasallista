from flask import Flask
from flask_cors import CORS
from logica import saludoLogica
app = Flask(__name__)
CORS(app)

@app.route('/')
def saludo():
    saludo = saludoLogica()
    return saludo

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2501)