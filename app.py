from flask import Flask,url_for, redirect, render_template, request
import pickle
import numpy as np
from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()

app = Flask(__name__, template_folder='template')

model = pickle.load(open('model.pkl', 'rb'))
@app.route('/')
def hello_world():
    return render_template('teach.html')

@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    print(request.form)
    int_features = [int(x) for x in request.form.values()]
    int_features = [label_encoder.transform(int_features)]
    final = [np.array(int_features)]
    print(int_features)
    print(final)
    result = model.predict(final)
    return result

    if result == 0:
        return render_template('teach.html', pred ='The price range of your course should be between Rs. 499 - 599 ')
    if result == 1:
        return render_template('teach.html', pred ='The price range of your course should be between Rs. 699 - 799 ')
    if result == 3:
        return render_template('teach.html', pred ='The price range of your course should be between Rs. 899 - 999 ')
    else:
        return render_template('teach.html', pred ='The price range of your course can be Rs. 1000+')


if __name__ == '__main__':
    app.run()
