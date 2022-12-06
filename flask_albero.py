from flask import Flask
from flask import render_template
from flask import jsonify
import logging

import socket
import json

app = Flask(__name__)

def send(command):
    HOST = "127.0.0.1"
    PORT = 33333

    json_cmd = {"cmd": command}
    json_cmd = json.dumps(json_cmd)

    response = None

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        logging.info(f"Connecting to {(HOST, PORT)}")
        s.connect((HOST, PORT))
        s.sendall(json_cmd.encode())
        if command == 'state':
            response = s.recv(20)
            logging.debug(f"Receiving: {response}")
        s.close()
    return response

@app.route('/test')
def test():
    logging.info("Test OK")
    return jsonify(success=True)

@app.route('/cmds/<command>', methods = ['GET', 'POST'])
def cmds(command):
    logging.debug(f"Enter cmds: {command}")
    send(command)

    return jsonify(success=True)

@app.route('/')
def hello_world():
    url_str='http://192.168.1.2:5000'
    response = send('state')
    logging.info(f"Response: {response}")
    if response is None:
        state = "Pause"
    else:
        json_msg = json.loads(response.decode())
        rsp = json_msg["rsp"]
        logging.info(f"Received response {rsp}")
        if rsp == "Pause":
            state = "Play"
        elif rsp == "Play":
            state = "Pause"

    return render_template('index.html', url=url_str, animation_state=state)

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(host="192.168.1.2")
