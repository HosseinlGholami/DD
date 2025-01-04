from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

# Function to create the Flask app and initialize SocketIO
def create_app():
    app = Flask(__name__, static_folder='../front/build', static_url_path='/')
    CORS(app)  # Enable CORS for all routes
    socketio = SocketIO(app, cors_allowed_origins="*")
    
    return app, socketio
