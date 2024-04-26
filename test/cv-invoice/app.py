import pytesseract
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import base64

import invoice
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/upload', methods=['POST'])
@cross_origin()
def upload_file():
    if 'image' not in request.json:
        return jsonify({'error': 'No image data found'})

    image_data = request.json['image']

    try:
        invoice.run_tesseract(image_data)
        return jsonify({'message': 'Image successfully uploaded'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
