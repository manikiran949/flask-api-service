from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    # Adding a timestamp and a color change to prove the update
    now = datetime.now().strftime("%H:%M:%S")
    return f"""
    <body style="background-color: #f0f8ff; font-family: sans-serif; text-align: center; padding-top: 50px;">
        <h1>🚀 GitOps Update Successful!</h1>
        <p><b>Last Deployed At:</b> {now}</p>
        <p><b>Status:</b> Running on Kubernetes (Minikube)</p>
    </body>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)