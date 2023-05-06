# imports
from http.server import BaseHTTPRequestHandler, HTTPServer

# import router
from src.routes.router import router

# data of server
HostName = 'localhost'
ServerPort = 3000

# server
class PythonServer(BaseHTTPRequestHandler):
    def do_GET(self):
        router(self)
    def do_POST(self):
        router(self)

if __name__ == '__main__':
    WebServer = HTTPServer((HostName, ServerPort), PythonServer)
    print(f"Server is running on {HostName}:{ServerPort}")

    try:
        WebServer.serve_forever()
    except KeyboardInterrupt:
        pass
    WebServer.server_close()
    print("Server is stopped!")
