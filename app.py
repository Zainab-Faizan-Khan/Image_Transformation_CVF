from flask import Flask, flash, request, redirect, send_file, url_for, render_template
from blur import convert_to_grayscale, blur_image #importing all the functions from blur.py
import os

app = Flask(__name__) 

 
app.secret_key = "secret key"

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 

#route to home
@app.route('/')
def home():
    return render_template('index.html') 
#route to gray scale function
@app.route('/grayscale', methods=['POST'])
def grayscale():
    if 'file' not in request.files:
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        return redirect('/')
    if file and allowed_file(file.filename):
        grayscale_img = convert_to_grayscale(file)
        return send_file(grayscale_img, mimetype='image/PNG')

@app.route('/blur', methods=['POST'])
def blur():
    if 'file' not in request.files:
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        return redirect('/')
    if file and allowed_file(file.filename):
        blurred_img = blur_image(file)
        return send_file(blurred_img, mimetype='image/PNG')


if __name__ == "__main__":
    app.debug='true'
    app.run(port=5000,debug=True)