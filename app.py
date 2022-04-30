import os
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',
                                    filename=filename))
    return render_template('main.html')
    
@app.route('/start', methods=['GET'])
def show_start():
    return render_template('start.html')
    
@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory('uploads', filename)
    
@app.route('/index', methods=['GET'])
def show_test():
    image_name = os.listdir('uploads')
    print(image_name)
    return render_template('index.html', image_name=image_name)

@app.route('/uploads', methods=['GET'])
def show_images():
    return render_template('test.html', image_name=image_names)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
