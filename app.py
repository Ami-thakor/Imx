from flask import Flask, render_template, request, send_from_directory
from enhancer import enhance_image
import os
import uuid

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
OUTPUT_FOLDER = os.path.join(BASE_DIR, 'outputs')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    image = request.files['image']
    uid = str(uuid.uuid4())
    input_path = os.path.join(UPLOAD_FOLDER, f"{uid}.png")
    output_path = os.path.join(OUTPUT_FOLDER, f"{uid}.png")
    image.save(input_path)

    enhance_image(input_path, output_path)
    if os.path.exists(input_path):
        os.remove(input_path)
    return {'url': f'/output/{uid}.png'}

@app.route('/output/<filename>')
def output(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

if __name__ == '__main__':
    app.run()
