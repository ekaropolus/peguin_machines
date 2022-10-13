
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_machine_learning():
    model_path = "mysite/models/clf.pkl"
    if request.method == "POST":
       # Unpickle classifier
       clf = joblib.load(model_path)
       # Get values through input bars
       culmen_length_mm = request.form.get("culmen_length_mm")
       culmen_depth_mm = request.form.get("culmen_depth_mm")
       flipper_length_mm = request.form.get("flipper_length_mm")
       body_mass_g = request.form.get("body_mass_g")
       # Put inputs to dataframe
       X = pd.DataFrame([[culmen_length_mm, culmen_depth_mm,flipper_length_mm,body_mass_g]], columns = ["culmen_length_mm", "culmen_depth_mm","flipper_length_mm","body_mass_g"])
       # Get prediction
       prediction = clf.predict(X)[0]
    else:
        prediction = ""
    return render_template("base.html", output = prediction)

