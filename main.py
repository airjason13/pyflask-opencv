# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
from flask import Flask, render_template, send_from_directory, request, redirect, url_for, Response
from global_def import *

app = Flask(__name__)
from routes import *

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    app.run(debug=True, port=flask_server_port)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
