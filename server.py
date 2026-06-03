"""HTTP server with CORS + Range support for serving FLV files."""
import http.server
import os
import argparse

DEFAULT_PORT = 5174
DEFAULT_DIR = r"D:\AI\AI-Split-live-record-douyin\recordings"

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=SERVE_DIR, **kwargs)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Range, Content-Type")
        self.send_header("Accept-Ranges", "bytes")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {args[0]}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Serve files with CORS and Range support")
    parser.add_argument("--dir", default=DEFAULT_DIR, help=f"Directory to serve (default: {DEFAULT_DIR})")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help=f"Port (default: {DEFAULT_PORT})")
    args = parser.parse_args()

    SERVE_DIR = os.path.abspath(args.dir)
    PORT = args.port

    print(f"Serving {SERVE_DIR} on http://localhost:{PORT}")
    print("Press Ctrl+C to stop")
    server = http.server.HTTPServer(("0.0.0.0", PORT), CORSRequestHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        server.server_close()
