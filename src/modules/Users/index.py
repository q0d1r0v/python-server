# imports
import json

# get users
def GetUsers(self): 
    data = {
        "name": "from Users"
    }
    self.send_response(200)
    self.send_header("Content-type", "application/json")
    self.end_headers()
    self.wfile.write(json.dumps(data).encode('utf-8'))