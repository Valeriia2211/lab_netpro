from flask import Flask, jsonify, request, abort
from flask_httpauth import HTTPBasicAuth
import json

app = Flask(__name__)
auth = HTTPBasicAuth()

ITEMS_FILE = 'items.json'
USERS_FILE = 'users.json'


def load_users():
    with open(USERS_FILE, 'r') as f:
        return json.load(f)


@auth.verify_password
def verify_password(username, password):
    users = load_users()
    if username in users and users[username] == password:
        return username


def load_items():
    with open(ITEMS_FILE, 'r') as f:
        return json.load(f)


def save_items(items):
    with open(ITEMS_FILE, 'w') as f:
        json.dump(items, f, indent=4)


@app.route('/items', methods=['GET'])
@auth.login_required
def get_all_items():
    return jsonify(load_items()), 200


@app.route('/items/<int:item_id>', methods=['GET'])
@auth.login_required
def get_item_by_id(item_id):
    items = load_items()
    for item in items:
        if item['id'] == item_id:
            return jsonify(item), 200
    abort(404)


@app.route('/items', methods=['POST'])
@auth.login_required
def add_item():
    items = load_items()
    data = request.json

    if not data or 'name' not in data or 'price' not in data or 'color' not in data:
        abort(400)

    new_id = items[-1]['id'] + 1 if items else 1

    new_item = {
        "id": new_id,
        "name": data['name'],
        "price": data['price'],
        "color": data['color']
    }

    items.append(new_item)
    save_items(items)

    return jsonify(new_item), 201


@app.route('/items/<int:item_id>', methods=['PUT'])
@auth.login_required
def update_item(item_id):
    items = load_items()
    data = request.json

    for item in items:
        if item['id'] == item_id:
            item['name'] = data.get('name', item['name'])
            item['price'] = data.get('price', item['price'])
            item['color'] = data.get('color', item['color'])

            save_items(items)
            return jsonify(item), 200

    abort(404)


@app.route('/items/<int:item_id>', methods=['DELETE'])
@auth.login_required
def delete_item(item_id):
    items = load_items()

    for item in items:
        if item['id'] == item_id:
            items.remove(item)
            save_items(items)
            return jsonify({"message": "Item deleted"}), 200

    abort(404)


if __name__ == '__main__':
    app.run(debug=True)
