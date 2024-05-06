import socket
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/hostname', methods=['GET'])
@cross_origin()
def getHostName():
    if (request.method=='GET'):
        data = {"hostname": socket.gethostname()}
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)