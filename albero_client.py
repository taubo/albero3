import socket
import logging
import json

json_cmd = {"cmd": "next"}
json_cmd = json.dumps(json_cmd)

def client():
    HOST = "127.0.0.1"
    PORT = 33333

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        logging.info(f"Connecting to {(HOST, PORT)}")
        s.connect((HOST, PORT))
        s.sendall(json_cmd.encode())
        s.close()

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    client()
