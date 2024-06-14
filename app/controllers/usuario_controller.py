from flask import jsonify, request
from app import app
from app.services.usuario_service import UsuarioService

@app.route("/usuario", methods=['GET'])
def usuario():
    data = request.get_json()
    id_usuario = data.get("id_usuario")
    rows = UsuarioService.obtener_usuario(id_usuario)
    usuario = [usuario.as_dict() for usuario in rows]
    return jsonify(usuario)

@app.route("/usuarios", methods=['GET'])
def usuarios():
    rows = UsuarioService.obtener_usuarios()
    usuarios = [usuarios.as_dict() for usuarios in rows]
    return jsonify(usuarios)

@app.route("/usuario_r", methods=['POST'])
def usuario_r():
    data = request.get_json()
    id_usuario = data.get("id_usuario")
    nombre_usuario = data.get("nombre_usuario")
    email_usuario = data.get("email_usuario")
    password_usuario = data.get("password_usuario")

    # Assuming UsuarioService.crear_usuario() returns an object with attributes
    nuevo_usuario = UsuarioService.crear_usuario(id_usuario, nombre_usuario, email_usuario, password_usuario)

    if nuevo_usuario:
        return jsonify({
            "mensaje": "Usuario ingresado exitosamente",
            "Usuario": {
                "id_usuario": nuevo_usuario.id_usuario,
                "nombre_usuario": nuevo_usuario.nombre_usuario,
                "email_usuario": nuevo_usuario.email_usuario,
                "password_usuario": nuevo_usuario.password_usuario
            }
        })
    else:
        return jsonify({
            "mensaje": "No se pudo crear el usuario"
        }), 400  # Example HTTP status code for bad request