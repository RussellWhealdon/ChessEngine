from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Chess World!'

@app.route('/move', methods=['POST'])
def make_move():
    data = request.json  # Assuming the move is sent as JSON
    user_move = data.get("move")
    print(f"Received move: {user_move}")
    # Placeholder for processing the move and determining the response
    engine_move = "e2e4"  # This will later be replaced with actual engine logic
    return jsonify({"engine_move": engine_move})

if __name__ == '__main__':
    app.run(debug=True)
