from http.server import BaseHTTPRequestHandler
from urllib import parse
import platform

class handle(BaseHTTPRequestHandler):
    def do_get(self):
        s=self.path
        url_components=parse.urlsplit(s)
        query_string_list=parse.parse_qsl(url_components.query)
        dic=dict(query_string_list)

        name=dic.get("name")

        if name:
            message = f"Aloha {name}"
        else:
            message ="Aloha stranger"
        message+=f"\nGreetings from Python version {platform.python_version()}"
        self.send_response(200)
        self.send_header('content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())