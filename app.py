from flask import Flask
import os
import socket

app = Flask(__name__)


@app.route("/")
def home():
    message = os.getenv("APP_MESSAGE", "Hello from Flask!")

    hostname = socket.gethostname()

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Containerized Flask Application</title>

        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f4f4f4;
                text-align: center;
                padding-top: 80px;
            }}

            .container {{
                background: white;
                width: 600px;
                max-width: 90%;
                margin: auto;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.15);
            }}

            h1 {{
                color: #333;
            }}

            .success {{
                color: green;
                font-weight: bold;
            }}

            .info {{
                margin-top: 20px;
                padding: 15px;
                background: #eee;
                border-radius: 6px;
            }}
        </style>
    </head>

    <body>

        <div class="container">

            <h1>Containerized Flask Application</h1>

            <p class="success">
                Flask application is running successfully!
            </p>

            <div class="info">
                <p><strong>Message:</strong> {message}</p>
                <p><strong>Container Hostname:</strong> {hostname}</p>
            </div>

            <p>
                Deployed using Docker, Amazon ECR and Amazon ECS.
            </p>

        </div>

    </body>
    </html>
    """


@app.route("/health")
def health():
    return {
        "status": "healthy"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)