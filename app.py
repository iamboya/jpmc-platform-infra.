from http.server import SimpleHTTPRequestHandler, HTTPServer

class JPMCHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"SECURE JPMC TRANSACTION INGRESS BACKEND: RUNNING\n")

print("🚀 Transaction Web Server initializing on Port 80...")
server = HTTPServer(('0.0.0.0', 80), JPMCHandler)
server.serve_forever()
