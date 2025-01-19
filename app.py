from flask import Flask, jsonify, request
import redis
import os
from dotenv import load_dotenv
import re
app = Flask(__name__)


url_regex = re.compile(
    r'^(?:http|https)://(?:\w+\.)?\w+\.\w+(?:/\S*)?$', re.IGNORECASE
)

load_dotenv()

redis_client = redis.Redis(
    host='redis-18856.c124.us-central1-1.gce.redns.redis-cloud.com',
    port=18856,
    decode_responses=True,
    username="default",
    password=os.getenv("REDIS_PASSWORD"),
)

@app.route('/shorten-url', methods=['GET'])
def shorten_url():
    data = request.get_json()

   
    if not data or 'url' not in data:
        return jsonify({"error": "Missing 'url' in request body"}), 400

    url = data['url']

    if not url_regex.match(url):
        return jsonify({"error": "Invalid URL"}), 400

    folder_name = 'short_urls'
    keys = redis_client.keys(f"{folder_name}/*")
    next_key = len(keys) + 1

    redis_key = f"{folder_name}/{next_key}"
    redis_client.set(redis_key, url)

    shortened_url = f"https://localhost:5000/{next_key}"

    return jsonify({"shortened_url": shortened_url}), 200