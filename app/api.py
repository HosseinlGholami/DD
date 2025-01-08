from flask import Blueprint,request, jsonify , current_app
from app.util.util import *

# Create a Blueprint for the API
api_blueprint = Blueprint('api', __name__)

# API route to start the dimension detection (example)
@api_blueprint.route('/start', methods=['POST'])
def start_detection():
    # 1- handle the request    
    data = request.json  # Get JSON payload from the request
    if not data or 'barcode' not in data:
        return jsonify({"error": "Invalid input. 'barcode' field is required."}), 400
    barcode = data['barcode']

    # 2- handle if is currently is processing the dimention
    working_mode = current_app.config['shared_resources'].working_mode.value
    if working_mode != "":
        return jsonify({"error": f"we are currently process the {working_mode}"}), 401
    current_app.config['shared_resources'].working_mode.value = barcode # put the working mode to the barcode

    # 3- send event to background process to start the dimention calculation
    bg_queue = current_app.config['shared_resources'].queues["bg_queue"]
    send_event_process(bg_queue,SRC.API_MAS.value,BgCommands.START_PROCESS.value)
    
    # Logic to start your background process or task
    return jsonify({"message": f"Dimension detection started on barcode {barcode}"}), 200

# API route to stop the dimension detection (if needed)
@api_blueprint.route('/stop', methods=['POST'])
def stop_detection():
    working_mode = current_app.config['shared_resources'].working_mode.value
    if working_mode == "":
        return jsonify({"error": "we dont have any active jobs"}), 200
    # we have to stop the process 
    # 1- change the working mode
    current_app.config['shared_resources'].working_mode.value = ""
    # 2- send event to background job to stop the calculation process
    bg_queue = current_app.config['bg_queue']
    send_event_process(bg_queue,SRC.API_MAS.value,BgCommands.STOP_PROCESS.value)

    # Logic to stop the background process
    return jsonify({"message": "Dimension detection stopped"}), 200

# Example of getting some status
@api_blueprint.route('/status', methods=['GET'])
def get_status():
    # Logic to return status or information from the process
    working_mode = current_app.config['shared_resources'].working_mode.value
    return jsonify({"status": f"Running --> {working_mode}"}), 200


# # TODO: IMAGE CALLIBRATION API
@api_blueprint.route('/img-calib', methods=['GET'])
def img_calib():
    # Logic to return status or information from the process
    camera_queue = current_app.config['shared_resources'].queues["camera_queue"]
    send_event_process(camera_queue,SRC.API_MAS.value,BgCommands.TAKE_PICTURE_ITEM.value)

    return jsonify({"status": f"Running --> {working_mode}"}), 200