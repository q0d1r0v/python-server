# imports
import json


def IndexModule(self):
    content_length = int(self.headers.get('Content-Length'))
    post_data = self.rfile.read(content_length)
    body = json.loads(post_data)
    body["request"] = "Hello from request"
    
    try:
        if(body["name"]):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(body).encode('utf-8'))
    except Exception as err:
        error_data = {
            "message": "We dont have all data!"
        }
        self.send_response(400)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(error_data).encode('utf-8'))
