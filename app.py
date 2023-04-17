from flask import Flask, render_template
app = Flask(__name__)

import pandas as pd 
df = pd.read_excel("https://github.com/wtitze/3E/blob/main/BikeStores.xls?raw=true", sheet_name="products")

@app.route("/", methods = ['GET'])
def home():
    return render_template("home.html")

@app.route("/", methods = ['get'])
def home():
    return render_template("categoria.html")

@app.route("/", methods = ['get'])
def home():
    return render_template("prezzo.html")

@app.route("/", methods = ['get'])
def home():
    return render_template("nome.html")

@app.route("/", methods = ['get'])
def home():
    return render_template("numero.html")

@app.route("/", methods = ['get'])
def home():
    return render_template("grafico.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)