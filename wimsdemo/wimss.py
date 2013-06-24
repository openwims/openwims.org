"""
This is an API configuration for the WIMsService on openwims.org

Note: This is hacked together. Fix this.
"""

import json
import socket

HOST = "localhost"
PORT = 9250

class WIMsService(object):

    """
    An API wrapper around the WIMsService object.
    """

    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = port
        self.sock = None

    def connect(self):
        if self.sock is not None:
            raise Exception("Socket is already open?")

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def close(self):
        if self.sock is not None:
            self.sock.close()
        self.sock = None

    def send(self, data):
        self.sock.sendall(json.dumps(data) + "\n")

    def recv(self):
        data = []
        while True:
            chunk = self.sock.recv(8192)
            if not chunk: break
            data.append(chunk)
        return json.loads(''.join(data))

    def analyze(self, text, version="1.0", request="parse"):
        kwargs = {
            "process-request": request,
            "ver": version,
            "text": text,
        }
        try:
            self.connect()
            self.send(kwargs)
            response = self.recv()
            self.close()
        finally:
            self.close()
        return response

if __name__ == "__main__":
    service = WIMsService()
    print json.dumps(service.analyze("The man hit the building with a bat."), indent=4)