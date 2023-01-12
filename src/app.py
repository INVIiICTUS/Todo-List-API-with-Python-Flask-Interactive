from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


todos = [ { "label": "My first task", "done": False } ]



@app.route('/todos', methods=['GET'])
def hello_world():
    todos_list = jsonify(todos)
    return todos_list


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    todos_list = jsonify(todos)
    return todos_list

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)