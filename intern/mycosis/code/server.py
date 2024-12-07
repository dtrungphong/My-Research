from flask import Flask, request, jsonify, render_template
import numpy as np
from PIL import Image
from model import PredictionModel


model = PredictionModel()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files['image']
    image = Image.open(file)

    output = model.process_result(image)
    mycosis = ['Candidiasis', 'Folliculitis', 'Pityriasis versicolor',
               'Seborrhoeic dermatitis and dandruff', 'Subcutaneous',
               'Tinea', 'Tinea nigra', 'White piedra']
    predicted_class = mycosis[np.argmax(output)]

    return jsonify({"predicted_class": predicted_class})

def get_ip():
    f = open('./config.txt',"r")
    data = f.read()
    host = data.split('\n')[0]
    port = data.split('\n')[1]
    return host,port

if __name__ == "__main__":
    host,port = get_ip()
    app.run(host=host,port=port,thread = True) 