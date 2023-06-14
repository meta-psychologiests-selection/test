import http.server
import socketserver
from http import HTTPStatus
import json


slots = [
    {
        "uuid": "9c76dbdd-2753-4d91-bcef-81d9c733cefc",
        "format": "online",
        "slot_start": "2023-06-15T15:00:00Z",
    },
    {
        "uuid": "3178b39e-3b26-439b-a84e-06ddce27b2a8",
        "format": "online",
        "slot_start": "2023-06-15T14:00:00Z",
    },
    {
        "uuid": "69089f05-e6db-4137-a54d-650e2a85359b",
        "format": "offline",
        "slot_start": "2023-06-15T16:00:00Z",
    },
    {
        "uuid": "28a142d0-fc10-49c4-8b3f-ad0abc57a8e8",
        "format": "offline",
        "slot_start": "2023-06-15T17:00:00Z",
    },
    {
        "uuid": "dbcfc11a-5537-4f49-9c7a-4223a118553e",
        "format": "offline",
        "slot_start": "2023-06-16T14:00:00Z",
    },
    {
        "uuid": "f48a6ad6-9140-49ea-8ea9-a552737e601d",
        "format": "online",
        "slot_start": "2023-06-16T15:00:00Z",
    },
    {
        "uuid": "9aa3035f-e8df-447a-b9c5-69685c58aff4",
        "format": "offline",
        "slot_start": "2023-06-16T16:00:00Z",
    },
    {
        "uuid": "6598c3e9-5bd0-481b-b1dc-f0c4aa04a05f",
        "format": "online",
        "slot_start": "2023-06-16T17:00:00Z",
    },
    {
        "uuid": "4cdd6f7a-599a-4b16-99e9-833f243c622b",
        "format": "online",
        "slot_start": "2023-06-16T18:00:00Z",
    },
]

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(bytes(json.dumps(slots), "utf-8"))


httpd = socketserver.TCPServer(("", 3100), Handler)
httpd.serve_forever()
