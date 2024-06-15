from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flasgger import Swagger # Lib de Swagger

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Evita warnings

db = SQLAlchemy(app)
CORS(app)
swagger = Swagger(app) # Integracion de Swagger

# Importa los controladores después de inicializar db para evitar problemas circulares
from app.controllers import reporte_controller
from app.controllers import usuario_controller
from app.controllers import movimiento_controller
from app.controllers import cuenta_controller
