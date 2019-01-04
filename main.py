#---FLASK APP---
from flask import Flask, render_template, request
from colorize import get_colored
import os
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def upload_file():
    gray_path = './static/gray.jpg'
    color_path = './static/color.jpg'
    if os.path.isfile(gray_path): os.remove(gray_path)
    if os.path.isfile(color_path): os.remove(color_path)

    if request.method == 'POST':
        f = request.files.get('file')
        if f is None:
        	return "No Image Uploaded!!!"
        f.save(gray_path)
        get_colored()
        return render_template("index.html", after=True)
    return render_template("index.html", after=False)

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1,firefox=1'
    response.headers['Cache-Control'] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response
