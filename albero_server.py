import logging
import socket
import selectors
import json

import led_animations as la
import board

sel = selectors.DefaultSelector()
leds_obj = la.LedAnimations(board.D18, 50)

def handle_message(message):
    json_msg = json.loads(message.decode())
    cmd = json_msg["cmd"]
    logging.info(f"Received command {cmd}")

    # si potrebbe usare una mappa
    if (cmd == "prev"):
        leds_obj.previous()
    elif (cmd == "next"):
        leds_obj.next()
    elif (cmd == "pause"):
        leds_obj.pause()
    elif (cmd == "play"):
        leds_obj.play()
    elif (cmd == "random"):
        leds_obj.random()

def accept_wrapper(sock):
    conn, addr = sock.accept()
    logging.info(f"Accepting connection from address {addr}")
    conn.setblocking(False)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    # se metto data=None mi tira eccezione
    sel.register(conn, events, data="bla")

def service_connection(key, mask, message_handler):
    logging.info(f"Performing service")

    sock = key.fileobj
    data = key.data

    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if not recv_data:
            logging.info("No data received")
            sel.unregister(sock)
            sock.close()
        else:
            logging.info(recv_data)
            message_handler(recv_data)
    if mask & selectors.EVENT_WRITE:
        logging.info("Writing data")

# put this inside a class and take the while True out
def server():
    HOST = "127.0.0.1"
    PORT = 33333

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setblocking(False)
    s.bind((HOST, PORT))
    s.listen()

    logging.info(f"Logging on {(HOST, PORT)}")
    sel.register(s, selectors.EVENT_READ, data=None)

    # conn, addr = s.accept()
    while True:
        leds_obj.animate()
        events = sel.select(timeout=0)
        for key, mask in events:
            # no data means that connection needs to be put in place
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask, handle_message)

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    server()
