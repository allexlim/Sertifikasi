from flask import Flask # untuk import flask
from flask import render_template as rt
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, file_required, file_allowed
from wtforms import SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SERTIFIKASI'
app.config['UPLOAD_PHOTO_DEST'] = 'UPLOADS'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

class UploadForm(FlaskForm):
    photo = FileField(
        validators = [file_allowed(photos, 'Hanya bisa mengunggah foto'),
        file_required('harus ada file yang diunggah')]
    )
    submit = SubmitField('upload')

@app.route('/')
def login():
    return rt("login.html")

@app.route('/homeGuest')
def homeGuest():
    return rt("home.html")

if __name__ == "__main__":
  app.run(debug=True)