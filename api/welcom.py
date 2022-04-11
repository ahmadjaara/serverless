from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    #  request is successful and you will get your response
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    message = "welcom , to Our website"
    self.wfile.write(message.encode())
    self.wfile.write(("\n"+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))).encode())
    return