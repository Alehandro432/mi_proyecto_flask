from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/enviar-datos', methods=['POST'])
def recibir_datos():
    datos = request.get_json()
    print("Datos recibidos:", datos)
    return jsonify({"message": "Datos recibidos correctamente"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
