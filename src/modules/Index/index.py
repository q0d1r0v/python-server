# imports
import json

def IndexModule(self):
    content_length = self.headers.get('Content-Length')
    print(self)
    data = {
        "name": "From Index"
    }
    self.send_response(200)
    self.send_header("Content-type", "application/json")
    self.end_headers()
    self.wfile.write(json.dumps(data).encode('utf-8'))
