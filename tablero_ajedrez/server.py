from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def tablero_uno():
    return render_template("tablero.html",
    fila=4,
    columna=4,
    )

@app.route("/<int:fila>")
def tablero_dos(fila):
    return render_template ("tablero.html", 
    fila=fila,
    columna=4,
    )

@app.route("/<int:fila>/<int:columna>")
def tablero_tres(fila, columna):
    return render_template ("tablero.html", 
    fila=fila,
    columna=columna,
    )

if __name__ == "__main__":
    app.run(debug=True)
