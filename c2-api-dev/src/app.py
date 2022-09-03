from flask import Flask, jsonify

app = Flask(__name__)

# Endpoint
@app.route('/')
def root():
    # Do some stuff
    variable = "some stuff"

    return jsonify({
        "success": True,
        "list": ["1", "2"],
        "bool": False,
        "number": 245,
        "map": {
            "key": "value",
            "map": {
                "key": variable
            }
        }
    })

@app.route('/list')
def list_data():
    return jsonify([1, 2, 3])