from flask import send_from_directory
from app import create_app
from app.websocket import register_websocket_events, ws_queue
from app.api import api_blueprint
from multiprocessing import Process, Manager

from app.background_process import *
from app.server_process import *
from app.esp32_process import *
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')


# Create Flask and SocketIO app
app, socketio = create_app()

# Register the WebSocket events
register_websocket_events(socketio)

# Register the API Blueprint
app.register_blueprint(api_blueprint)

# Serve the React app
@app.route('/')
def serve_react_app():
    return send_from_directory(app.static_folder, 'index.html')

# Serve static files
@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

class SharedResources:
    def __init__(self, manager):
        self.queues = {
            "esp32_queue": manager.Queue(),
            "server_queue": manager.Queue(),
            "bg_queue": manager.Queue(),
            "ws_queue": manager.Queue(),
            "csv_queue": manager.Queue(),
            "camera_queue": manager.Queue()
        }
        self.processes = {}
        self.working_mode = manager.Value('s', "")


if __name__ == '__main__':
    # Initialize shared resources
    manager = Manager()
    shared_resources = SharedResources(manager)

     # Add shared resources to Flask app config
    app.config['shared_resources'] = shared_resources

    # bg PROCESS
    process = Process(target=bg_controller, args=(shared_resources,))
    process.start()

    # SERVER PROCESS
    # process = Process(target=server_connection, args=(shared_resources,))
    # process.start()

    #ESP32 PROCESS
    process = Process(target=esp32_process, args=(shared_resources,))
    process.start()

    # Run the Flask-SocketIO server
    socketio.run(app, host='0.0.0.0', port=5003, debug=True, use_reloader=False)
