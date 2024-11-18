from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {
        "done": True,
        "label": "Sample Todo 1"
    },
    {
        "done": True,
        "label": "Sample Todo 2"
    }
]

# Ruta para listar todos los todos
@app.route('/todos', methods=["GET"])
def get_Todos():
    return jsonify(todos), 200

# Ruta para agregar un nuevo item a todos
@app.route('/todos', methods=['POST'])
def post_todo():
    # Sacamos del body el item a postear en json
    item_from_request_body = request.json

    # Verificar si el JSON tiene datos válidos
    if not item_from_request_body:  # Si el JSON está vacío
        return jsonify({"error": "El cuerpo JSON está vacío"}), 400
    
    todos.append(item_from_request_body)
    return jsonify(item_from_request_body), 201  # Retorna el item agregado con un código 201

# Ruta para eliminar un todo por su índice
@app.route("/todos/<int:posy>", methods=["DELETE"])
def delete_todo(posy):
    if posy < 0:
        return jsonify({"error": "Posición inválida, enviaste un valor negativo"}), 400

    if posy >= len(todos):  # Cambié > por >=
        return jsonify({"error": "Posición inválida, enviaste un valor mayor al total de elementos en la lista"}), 400

    # Eliminar el item en la posición indicada
    deleted_item = todos.pop(posy)
    return jsonify(deleted_item), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

#EnriqueLopez4G
#latam-36