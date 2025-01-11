from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/enviar-datos', methods=['POST'])
def recibir_datos():
    datos = request.get_json()
    nombre = datos.get('nombre', 'N/A')
    ubicacion = datos.get('ubicacion', 'N/A')
    print("Datos recibidos:", datos)
    return jsonify({"message": "Datos recibidos correctamente", "nombre": nombre, "ubicacion": ubicacion}), 200

if __name__ == '__main__':
    app.run(debug=True)
