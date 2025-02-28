from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello, this is a test API!"})

@app.route('/status')
def status():
    return jsonify({"status": "API is running!"})

# ✅ New POST endpoint to receive data
@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()  # Get JSON data from request
    if not data:
        return jsonify({"error": "No data received"}), 400
    return jsonify({"received": data})  # Return received data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
