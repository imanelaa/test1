#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, SimpleHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
# import mon_module
import json
# globals
listcmd=["bouton1","bouton2"]

class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        cmd=self.path[1:8]
	# HERE YOU SHOULD PROBABLY DO SOMETHING WITH cmd
        a_file = open("buttons.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        json_object[cmd]['clicks'] = int(json_object[cmd]['clicks']) + 1
        a_file = open("buttons.json", "w")
        json.dump(json_object, a_file)
        a_file.close()
        print(json_object)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(json.dumps(json_object, ensure_ascii=False), 'utf-8'))
        return 

class RouteHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path[1:8] in listcmd:
            return GetHandler.do_GET(self)
        else:
            super(RouteHandler,self).do_GET()

class ThreadingSimpleServer(ThreadingMixIn,HTTPServer): pass

if __name__ == '__main__':
    server=ThreadingSimpleServer(('0.0.0.0',8000),RouteHandler)
    print('Starting server, use <Ctrl-C> to stop')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        a_file = open("buttons.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        json_object['bouton1']['clicks'] = 0
        json_object['bouton2']['clicks'] = 0
        a_file = open("buttons.json", "w")
        json.dump(json_object, a_file)
        a_file.close()
        server.server_close()

