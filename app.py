from flask import Flask, jsonify, render_template, request
import numpy as np
import pickle
import os
app = Flask(__name__)

model= pickle.load(open('C:\\Users\\harno\\OneDrive\\Desktop\\SEMESTER 7\\MAJOR PROJECT\\flask demo\\cp.pkl', 'rb'))

 
@app.route('/')

def frontp():
  return render_template('frontp.html')

@app.route('/btn2.html', methods=['POST','GET'])
def btn2():
    if request.method=='POST':
        Year = float(request.form['Year'])
        State_UT = float(request.form['State/UT'])
        Crime_Type = float(request.form['Crime'])
      
        X = np.asarray([[Year,State_UT,Crime_Type]])
        prediction = model.predict(X)
        return render_template('C:\\Users\\harno\\OneDrive\\Desktop\\SEMESTER 7\\MAJOR PROJECT\\flask demo\\templates\\resultf.html', prediction = prediction)
        X = X.reshape(1, -1)
    else:
        return render_template('btn2.html')
 
if __name__ == '__main__':
 
    app.run()