from flask import Flask, request, jsonify
import os

app = Flask(__name__)
app.debug = True
app.config['UPLOAD_FOLDER'] = './upload_dir'

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        return jsonify("file uploaded successfully..!")
    return '''
    <form method='post' enctype='multipart/form-data'>
    <input type='file' name='file'>
    <input type='submit' value='submit'>
    </form>
    '''

if __name__ == "__main__":
    app.run()