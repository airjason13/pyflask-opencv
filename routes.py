import os
import time
import cv2

from main import app
from flask import Flask, render_template, send_from_directory, request, redirect, url_for, Response, json
from global_def import *

video = cv2.VideoCapture(0)

@app.route("/")
def index():

    return render_template("index.html", title=title)

def gen_video():

    #video = cv2.VideoCapture(0)
    while True:
        ret, frame = video.read()
        if not ret:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        time.sleep(0.03)

@app.route('/video_feed')
def video_feed():

    return Response(gen_video(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    return

