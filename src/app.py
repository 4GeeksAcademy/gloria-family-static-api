"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Se instancia la familia; la inicialización interna crea los miembros por defecto.
jackson_family = FamilyStructure("Jackson")

# Manejo de errores personalizados
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Genera un sitemap con todos los endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:id>', methods=['GET'])
def get_single_member(id):
    member = jackson_family.get_member(id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"error": "Member not found"}), 404

@app.route('/member', methods=['POST'])
def create_member():
    member = request.json
    new_member = jackson_family.add_member(member)
    # Se retorna el miembro recién creado en formato JSON.
    return jsonify(new_member), 200

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_single_member(id):
    success = jackson_family.delete_member(id)
    if success:
        return jsonify({"done": True}), 200
    else:
        return jsonify({"error": "Member not found"}), 404

# Se ejecuta la aplicación únicamente si se corre este módulo directamente
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
