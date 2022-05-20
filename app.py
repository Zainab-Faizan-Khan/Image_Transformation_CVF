from flask import Flask, flash, request, redirect, send_file, url_for, render_template
from blur import convert_to_grayscale, blur_image , sketchimage, sharpen_image , contrast_image, dull_image,transpose_image #importing all the functions from blur.py
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

@app.route('/sketch', methods=['POST'])
def sketch():
    if 'file' not in request.files:
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        return redirect('/')
    if file and allowed_file(file.filename):
        sketch_img = sketchimage(file)
        return send_file(sketch_img, mimetype='image/PNG')

@app.route('/sharpen', methods=['POST'])
def sharpen():
    if 'file' not in request.files:
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        return redirect('/')
    if file and allowed_file(file.filename):
        sharpen_img = sharpen_image(file)
        return send_file(sharpen_img, mimetype='image/PNG')

@app.route('/contrast', methods=['POST'])
def contrast():
    if 'file' not in request.files:
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        return redirect('/')
    if file and allowed_file(file.filename):
        contrast_img = contrast_image(file)
        return send_file(contrast_img, mimetype='image/PNG')

@app.route('/dull', methods=['POST'])
def dull():
    if 'file' not in request.files:
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        return redirect('/')
    if file and allowed_file(file.filename):
        dull_img = dull_image(file)
        return send_file(dull_img, mimetype='image/PNG')

@app.route('/transpose', methods=['POST'])
def transpose():
    if 'file' not in request.files:
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        return redirect('/')
    if file and allowed_file(file.filename):
        transpose_img = transpose_image(file)
        return send_file(transpose_img, mimetype='image/PNG')

if __name__ == "__main__":
    app.debug='true'
    app.run(port=5000,debug=True)