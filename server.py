import SimpleHTTPServer
import SocketServer

PORT = 1337

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "[+] Posse listening on port", PORT
httpd.serve_forever()
