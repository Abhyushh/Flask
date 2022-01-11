from flask import Flask
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)


@app.route("/")
def hello_world():
    return "<p>jksdcvnhjksdfvh!</p>"


if __name__ == "_main_":
    app.run()
