from flask import jsonify, request
from app import app
from app.services.cuenta_service import CuentaService
from flasgger import swag_from

@app.route("/cuenta", methods=['GET'])
@swag_from('../swagger_config/cuenta.yml')
def cuenta():
    data = request.args
    numero_cuenta = data.get("numero_cuenta")
    rows = CuentaService.obtener_cuenta(numero_cuenta)
    cuenta = [cuenta.as_dict() for cuenta in rows]
    return jsonify(cuenta)

@app.route("/cuentas", methods=['GET'])
#@swag_from('swagger_config/cuentas.yml')
def cuentas():
    rows = CuentaService.obtener_cuentas()
    cuentas = [cuenta.as_dict() for cuenta in rows]
    return jsonify(cuentas)

@app.route("/cuenta_r", methods=['POST'])
#@swag_from('swagger_config/cuenta_r.yml')
def cuenta_r():
    data = request.get_json()
    numero_cuenta = data.get("numero_cuenta")
    tipo_cuenta = data.get("tipo_cuenta")
    saldo_cuenta = data.get("saldo_cuenta")
    id_usuario = data.get("id_usuario")

    nueva_cuenta = CuentaService.crear_cuenta(numero_cuenta, tipo_cuenta, saldo_cuenta, id_usuario)

    if nueva_cuenta:
        return jsonify({
            "mensaje": "Cuenta ingresada exitosamente",
            "Cuenta": {
                "numero_cuenta": nueva_cuenta.numero_cuenta,
                "tipo_cuenta": nueva_cuenta.tipo_cuenta,
                "saldo_cuenta": nueva_cuenta.saldo_cuenta,
                "id_usuario": nueva_cuenta.id_usuario
            }
        })
    else:
        return jsonify({"mensaje": "No se pudo crear la Cuenta"}), 400
