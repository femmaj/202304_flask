from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "superhipersecretkey"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    session["nombre"] = request.form["nombre"]
    session["ubicacion"] = request.form["ubicacion"]
    session["lenguaje"] = request.form["lenguaje"]
    if request.form["comentario"]:
        session["comentario"] = request.form["comentario"]
    else:
        session["comentario"] = "Sin comentarios"
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)