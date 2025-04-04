from flask import Flask, Response, request
import requests

app = Flask(__name__)

KOYEB_BASE = "https://alright-faina-eypz-god-0512c786.koyeb.app/"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    url = f"{KOYEB_BASE}/{path}"
    resp = requests.get(url, params=request.args)
    return Response(resp.content, status=resp.status_code, content_type=resp.headers.get('Content-Type'))
