from app import db
from app.models.usuario import Usuario

class UsuarioRepository:
    @staticmethod
    def obtener_usuario(id_usuario):
        return Usuario.query.filter_by(id_usuario=id_usuario).all()
    
    @staticmethod
    def obtener_usuarios():
        return Usuario.query.all()

    @staticmethod
    def crear_usuario(id_usuario, nombre_usuario, email_usuario,password_usuario):
        nuevo_usuario = Usuario(
            id_usuario=id_usuario,
            nombre_usuario=nombre_usuario,
            email_usuario=email_usuario,
            password_usuario=password_usuario
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        return nuevo_usuario
