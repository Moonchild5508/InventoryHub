from flask import Flask, jsonify, request
import db

app = Flask(__name__)

@app.route('/inventory', methods=['GET'])
def get_inventory():
    items = db.get_inventory()
    return jsonify({"status": "success", "data": items})

@app.route('/inventory', methods=['POST'])
def add_inventory():
    item = request.json
    db.add_item(item)
    return jsonify({"status": "success", "message": "Item added successfully"})

if __name__ == "__main__":
    app.run(debug=True)
