from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# Global variable to store data
received_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post-data', methods=['POST'])
def post_data():
    data = request.form.to_dict()
    received_data.append(data)
    socketio.emit('new_data', data)  # Broadcast new data to all clients
    return jsonify(data), 200

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=80)
