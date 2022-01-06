from flask import Flask
import cv2

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"


if __name__ == "_main_":
    app.run()
