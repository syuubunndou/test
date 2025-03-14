from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORSを許可

@app.route('/get_message', methods=['GET'])
def get_message():
    return jsonify({"message": "foo"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
