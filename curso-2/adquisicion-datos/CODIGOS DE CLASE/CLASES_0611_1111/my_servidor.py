from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hola: Gonzalo!</p>"

@app.route("/icai")
def hola_icai():
    return "<p>Hola: <b>ICAI!</b></p>"

@app.route("/gato")
def hola_gato():
    return render_template("gato.html", nombre="Mateo")

@app.route("/formulario_saludar")
def formulario_saludar():
    return render_template("formulario_saludar.html")

@app.route("/saludar", methods=["POST"])
def saludar():
    name = request.form.get("name")
    greeting = request.form.get("greeting")

    return render_template("saludar.html", name=name, greeting=greeting)