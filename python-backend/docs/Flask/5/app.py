from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def process_data():
    data = request.json
    # Process the data (this is just a placeholder)
    processed_data = {"message": "Data received", "data": data}
    return jsonify(processed_data), 200
@app.route('/api/data', methods=['GET'])
def get_data():
    # Return some dummy data
    dummy_data = {"message": "This is dummy data"}
    return jsonify(dummy_data), 200     