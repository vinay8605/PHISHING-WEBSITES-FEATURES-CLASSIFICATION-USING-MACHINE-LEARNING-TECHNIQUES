from flask import Flask,render_template,request
import pickle
import numpy as np

pipeline_ls = pickle.load(open('phishing.pkl','rb'))

app = Flask(__name__)

@app.route('/vinay')
def index():
    return render_template('index.html')

@app.route('/Result',methods=['POST'])
def predict():
    URL = (request.form.get('URL'))
    # prediction
    result = pipeline_ls.predict([URL])
    


    return render_template('Result.html',result=str(result))


if __name__ == '__main__':
    app.run(debug=True)