from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np


app = Flask(__name__, template_folder="template")

reg = pickle.load(open("model.pkl", "rb"))




@app.route("/")
def hello_worl():
     return render_template("main.html")

@app.route("/about")
def hello_wor():
     return render_template("about.html")

@app.route("/choose")
def hello_wo():
     return render_template("choose.html")

@app.route("/remedy")
def hello_wr():
     return render_template("sol.html")

@app.route("/test")
def hello1():
     return render_template("test.html")



@app.route("/predict", methods=["POST"])
def home():
    data1 = float(request.form["b"])
    data2 = float(request.form["b"])
    data3 = float(request.form["c"])
    data4 = float(request.form["d"])
    d5 = float(request.form["e"])
    d6 = float(request.form["f"])
    d7 = float(request.form["g"])
    d8 = float(request.form["h"])
    d9 = float(request.form["i"])
    d10 = float(request.form["j"])
    d11 = float(request.form["k"])
    d12 = float(request.form["l"])
    d13 = float(request.form["m"])
    d14 = float(request.form["n"])
    d15 = float(request.form["o"])
    d16 = float(request.form["p"])
    d17 = float(request.form["q"])
    d18 = float(request.form["r"])
    d19 = float(request.form["s"])
    d20 = float(request.form["t"])
    d21 = float(request.form["u"])
    d22 = float(request.form["v"])
    d23 = float(request.form["w"])
    d24 = float(request.form["x"])
    d25= float(request.form["y"])
    d26 = float(request.form["z"])
    d27 = float(request.form["za"])
   
   

    arr = np.array(
        [
            [
                data1,
                data2,
                data3,
                data4,
                d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,
                d17,d18,d19,d20,d21,d22,d23,d24,d25,d26,d27
                            ]
        ]
    )
    pred = reg.predict(arr)
    print(pred)
    return render_template("index.html", data=pred)

reg1 = pickle.load(open("model1.pkl", "rb"))

@app.route("/test1")
def hello2():
     return render_template("test2.html")


@app.route("/predict", methods=["POST"])
def hom():
    data1 = float(request.form["b"])
    data2 = float(request.form["b"])
    data3 = float(request.form["c"])
    data4 = float(request.form["d"])
    d5 = float(request.form["e"])
    d6 = float(request.form["f"])
    d7 = float(request.form["g"])
    d8 = float(request.form["h"])
    d9 = float(request.form["i"])
    d10 = float(request.form["j"])
    d11 = float(request.form["k"])
    d12 = float(request.form["l"])
    d13 = float(request.form["m"])
    d14 = float(request.form["n"])
    d15 = float(request.form["o"])
    d16 = float(request.form["p"])
    d17 = float(request.form["q"])
    d18 = float(request.form["r"])
    d19 = float(request.form["s"])
    d20 = float(request.form["t"])
    d21 = float(request.form["u"])
    d22 = float(request.form["v"])
    d23 = float(request.form["w"])
    d24 = float(request.form["x"])
    d25= float(request.form["y"])
    d26 = float(request.form["z"])
    d27 = float(request.form["za"])
    d28 = float(request.form["zb"])
    d29 = float(request.form["zc"])
    d30 = float(request.form["zd"])
    d31 = float(request.form["ze"])
    d32 = float(request.form["zf"])
    d33 = float(request.form["zg"])
    d34 = float(request.form["zh"])
    d35 = float(request.form["zi"])
    d36 = float(request.form["zj"])
    d37 = float(request.form["zk"])
   
   

    arr = np.array(
        [
            [
                data1,
                data2,
                data3,
                data4,
                d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,
                d17,d18,d19,d20,d21,d22,d23,d24,d25,d26,d27,
                d28,d29,d30,d31,d32,d34,d35,d36,d37
                            ]
        ]
    )
    pred1 = reg1.predict(arr)
    print(pred1)
    return render_template("index.html", data=pred1)




if __name__ == "__main__":
    app.run(debug=True)
