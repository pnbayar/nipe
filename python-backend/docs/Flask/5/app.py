from flask import Flask, request, jsonify

app = Flask(__name__)
 

@app.route('/api/data', methods=['POST'])
def process_data():
    data = request.json
    # Process the data (this is just a placeholder)
    processed_data = {"message": "Post Data received", "data": data}
    return jsonify(processed_data), 200
@app.route('/api/data', methods=['GET'])
def get_data():
    # Return some dummy data
    dummy_data = {"message": "This is dummy data"}
    return jsonify(dummy_data), 200     

# Run the Flask app
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)