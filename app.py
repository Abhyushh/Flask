from flask import Flask, render_template, Response, request
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)


def generate_frames():
    while True:

        # read the camera frame
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route('/video/61575d1c85fd1cc36010924b')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "_main_":
    app.run()
