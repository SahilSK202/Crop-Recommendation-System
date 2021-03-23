from flask import Flask, render_template, request, redirect
import pickle
import numpy as np


app = Flask(__name__)
model = pickle.load(open('Final_GaussianNB_Model.pkl', 'rb'))



@app.route('/' , methods=['GET' , 'POST'])
def Home():
        return render_template('index.html')

@app.route('/predict', methods=['GET' , 'POST'])
def predict():
    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['pottasium'])
        Temp = float(request.form['temperature'])
        Humid = float(request.form['humidity'])
        Ph = float(request.form['ph'])
        Rain = float(request.form['rainfall'])

        sample = [N ,P ,K ,Temp , Humid , Ph , Rain]

        single_sample = np.array(sample).reshape(1, -1)
        Prediction = model.predict(single_sample)
        Prediction = Prediction.item().upper()
        print(Prediction)

        sample.append(Prediction)

        return render_template('predict.html', sample = sample)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
