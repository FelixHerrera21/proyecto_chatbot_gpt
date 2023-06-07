from waitress import serve
from app import app  # Reemplaza "tu_aplicacion" con el nombre del archivo principal de tu aplicación Flask

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000, threads=1)
