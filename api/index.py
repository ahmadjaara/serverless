from http.server import BaseHTTPRequestHandler
from urllib import parse
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
              
        
        if "name" in dic:
            message = "Hi, " + dic["name"] + "!"
        else:
            message = "Hi, stranger!"  

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()  
        self.wfile.write(message.encode(),str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
        return