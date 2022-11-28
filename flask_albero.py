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

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        logging.info(f"Connecting to {(HOST, PORT)}")
        s.connect((HOST, PORT))
        s.sendall(json_cmd.encode())
        s.close()

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
    return render_template('index.html', url=url_str)

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(host="192.168.1.2")
