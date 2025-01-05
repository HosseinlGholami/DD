from flask_socketio import emit
from flask import current_app

# Initialize the queue for communication

def register_websocket_events(socketio,shared_resources):

    ws_queue = shared_resources.queues["ws_queue"]

    # WebSocket event to handle new connections
    @socketio.on('connect')
    def handle_connect():
        print('Client connected')

    # WebSocket event to handle disconnections
    @socketio.on('disconnect')
    def handle_disconnect():
        print('Client disconnected')

    # Function to send data to WebSocket clients every second
    def send_data_to_clients():
        while True:
            if not ws_queue.empty():
                data = ws_queue.get()  # Get data from the queue
                socketio.emit('meta', data)  # Emit to all WebSocket clients
            socketio.sleep(0.01)  # Non-blocking sleep to avoid blocking the event loop

    # Start the WebSocket data sender as a background task
    socketio.start_background_task(target=send_data_to_clients)
