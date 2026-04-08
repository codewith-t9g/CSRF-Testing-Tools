#!/usr/bin/env python3
"""
Simple HTTP server for CSRF Testing Tools
Run: python3 server.py
Then open: http://localhost:8000/formbuilder.html
"""

import http.server
import socketserver
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add headers to ensure Referer is sent with form submissions
        self.send_header('Referrer-Policy', 'always')
        super().end_headers()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}/")
    print(f"Open http://localhost:{PORT}/formbuilder.html in your browser")
    print("Press Ctrl+C to stop the server")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")
