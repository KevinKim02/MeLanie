import os
from app import app
# from .model import load

#image libraries
from PIL import Image
import cv2
import numpy as np

# import numpy as np
import keras.models
# from keras.models import model_from_json
# from scipy.misc.pilutil import imread, imshow

import tensorflow as tf
import efficientnet.tfkeras
from tensorflow import keras

# global model

from flask import Flask, flash, render_template, request, redirect, url_for

ALLOWED_EXTENSIONS = {'jpg'}
app.config['SECRET_KEY'] = "5f352379324c22463451387a0aec5d2g"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return """
    <h1 style='color: red;'>I'm a red H1 heading!</h1>
    <p>This is a lovely little paragraph</p>
    <code>Flask is <em>awesome</em></code>
    """

#app.config["IMAGE_UPLOADS"] = "/mnt/c/wsl/projects/pythonise/tutorials/flask_series/app/app/static/img/uploads"
@app.route("/upload-image", methods=('GET', 'POST'))
def upload_image():
    print('upload')
    if request.method == "POST":
        print("this is a post request")
        # check if the post request has the file part
        if 'image' not in request.files:
            print("no file part")
            flash('No file part')
            return redirect(request.url)
        file = request.files['image']
        # if user does not select file, browser also submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # filename = secure_filename(file.filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('uploaded_file',
            #                         filename=filename))

            read = lambda imname: np.asarray(Image.open(imname).convert("RGB"))
            img = read(file)
            img = cv2.resize(img, (224,224))

            img = np.array(img)/255.
            img = np.array(img)/255.
            img = np.reshape(img,[1,224,224,3])
            
            print("image")

            # return redirect(request.url)
            # with graph.as_default():
            model = tf.keras.models.load_model('C:/Users/aarti/Desktop/VS Code projects/MeLanie/app/model/model2.h5')

            out = model.predict(img)
            maxIndex = np.argmax(out)
            print(out)
            print(maxIndex)
            
            if(maxIndex):
                str1 = "MALIGNANT :" + str(out[0][maxIndex])
            else:
                str1 = "BENIGN: " + str(out[0][maxIndex])
            return str1
            


    
    return render_template("public/upload_image.html")
    #, user_image = imag
    # e, prediction = response) if (request.method == "POST") else render_template("public/upload_image.html")

