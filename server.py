from flask import Flask, Response
from prometheus_client import Counter, generate_latest, REGISTRY

app = Flask(__name__)

# Define a counter metric with labels
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint'])

@app.route('/')

def home():
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    return "Server is running and available!"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(REGISTRY), content_type='text/plain')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)