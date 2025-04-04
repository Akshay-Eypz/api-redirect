from flask import Flask, Response, request
import requests

app = Flask(__name__)

KOYEB_BASE = "https://prime-kissee-amv-stream-0e7b4e5b.koyeb.app/"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    url = f"{KOYEB_BASE}/{path}"
    resp = requests.get(url, params=request.args)
    return Response(resp.content, status=resp.status_code, content_type=resp.headers.get('Content-Type'))
