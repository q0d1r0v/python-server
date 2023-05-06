# imports
import json

def NotFoundRoute(self):
    data = {
        "message": "Not found"
    }
    self.send_response(404)
    self.send_header("Content-type", "application/json")
    self.end_headers()
    self.wfile.write(json.dumps(data).encode('utf-8'))