import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

class JPMCHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Establish the log directory path boundary
        os.makedirs("logs", exist_ok=True)
        
        # Append the transactional request event to the file system disk
        with open("logs/transactions.log", "a") as log_file:
            log_file.write("EVENT: Secure incoming transactional request processed mapping baseline HTTP 200\n")
            
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"SECURE JPMC TRANSACTION INGRESS BACKEND: RUNNING\n")

print("🚀 Transaction Web Server initializing on Port 80...")
server = HTTPServer(('0.0.0.0', 80), JPMCHandler)
server.serve_forever()

