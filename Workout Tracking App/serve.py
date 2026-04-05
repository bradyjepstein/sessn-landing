import http.server
import os

os.chdir("/Users/bradyepstein/Desktop/Workout Tracking App")
handler = http.server.SimpleHTTPRequestHandler
server = http.server.HTTPServer(("", 8090), handler)
print("Serving on http://localhost:8090")
server.serve_forever()
