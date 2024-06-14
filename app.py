from flask import Flask, jsonify, request, session
from flask_cors import CORS
from database import conectar_database
from datetime import datetime as dt

app = Flask(__name__)
CORS(app)


#------------------------------------------------------------------------------------
# Reporte de la Cuenta de un Usuario
@app.route("/reporte", methods=['GET'])
def reporte():
    
    data = request.get_json()
    id_usuario = str(data.get("id_usuario"))
    conn = conectar_database()
    cur = conn.cursor()
    cur.execute('SELECT * FROM reporte_cuenta WHERE id_usuario = %s', (id_usuario,))
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(rows)