import os
from flask import Flask, render_template, request, flash

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
ALLOWED_EXTENSIONS = set(['pdf'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    target = os.path.join(APP_ROOT, 'pdf-files/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist('file'):
        if allowed_file(file.filename):
            print(file)
            filename = file.filename
            destination = '/'.join([target, filename])
            print(destination)
            file.save(destination)
        else:
            return render_template('error.html')
            # flash('There was an error! Was the file selected a PDF?')

    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug = True)
