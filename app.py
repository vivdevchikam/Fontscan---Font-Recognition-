from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from font_recognition import predict_font  # Your prediction function

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Get prediction
            prediction = predict_font(filepath)
            
            return render_template('index.html', 
                                 prediction=prediction,
                                 uploaded_image=filename)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)