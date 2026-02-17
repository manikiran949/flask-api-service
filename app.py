from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def home():
    # Fetch system info 
    pod_name = socket.gethostname()
    app_version = os.getenv("APP_VERSION", "v1.0.0")
    
    return f"""
    <html>
        <head><title>Microservice Dashboard</title></head>
        <body style="font-family: sans-serif; margin: 40px;">
            <h2>🚀 GitOps Deployment Successful</h2>
            <hr>
            <p><strong>Status:</strong> Online</p>
            <p><strong>Pod ID:</strong> {pod_name}</p>
            <p><strong>Version:</strong> {app_version}</p>
            <p><strong>Namespace:</strong> flask-api</p>
            <hr>
            <small>Automatically deployed via Argo CD</small>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)