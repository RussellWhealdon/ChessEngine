from flask import Flask, request, jsonify
import chess

app = Flask(__name__)

# Initialize a global chess board
board = chess.Board()

@app.route('/')
def hello_world():
    return 'Hello, Chess World!'

@app.route('/move', methods=['POST'])
def make_move():
    if not board.is_game_over():
        data = request.json
        user_move = data.get("move")
        
        try:
            move = chess.Move.from_uci(user_move)
            if move in board.legal_moves:
                board.push(move)
                # Placeholder for AI move logic
                response = {"status": "success", "move_made": user_move}
            else:
                response = {"status": "error", "message": "Illegal move"}
        except ValueError:
            response = {"status": "error", "message": "Invalid move format"}
    else:
        response = {"status": "game over", "message": "The game is over"}
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
