import os

from flask import Flask, flash
from werkzeug.utils import secure_filename
from flask import request, redirect, url_for, render_template

from pictures.picture import PictureResizer


app = Flask(__name__)
upload_dir = os.path.join("src", "static", "upload")
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = upload_dir


@app.route('/')
def upload_form() -> str:
    """
    Render HTML format from the source file.
    """
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']

    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)

    if file:
        filename = secure_filename(file.filename)  # type: ignore
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        process_image(filename)

        return render_template(
            'upload.html',
            filename=f"resized_{filename}"
        )

    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename: str):
    """
    Render the images saved in the static/upload directory.

    :param filename: a name of the file.
    :type filename: str
    """
    return redirect(url_for('static', filename='upload/' + filename), code=301)


def process_image(filename: str) -> None:
    """
    Render the processed image from the static/upload/* directory.

    :param filename: a name of the file.
    :type filename: str
    """
    modified = PictureResizer(
        os.path.join("src", "static", "upload", filename), filename
    )
    init_img = modified.initiate_image()
    current_dims = modified.get_dimensions(init_img)
    status = modified.resize_image(init_img)

    if status:
        print(f"Origin: {current_dims}")
        flash('Image successfully uploaded and displayed below')


if __name__ == "__main__":
    app.run(debug=True)
