import pickle
from flask import Flask, request, jsonify, url_for, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)
regmodel = pickle.load(open('regmodel.pkl','rb')) # Loading the model
scalar = pickle.load(open('scaling.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])

def predict_api():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data = scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output = regmodel.predict(new_data)
    print(output[0]) # As it is a 2D array taking the first value
    return jsonify(output[0])

if __name__=="__main__":
    app.run(debug=True)

