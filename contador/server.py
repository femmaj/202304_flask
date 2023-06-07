from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "supersecreta"

@app.route("/contador")
def index():
    if "contador" not in session:
        session["contador"] = 1
    else:
        session["contador"] += 1
    return render_template("contador.html")


@app.route("/destroy_session")
def reset():
    session.pop("contador")
    return redirect("index")

if __name__ == "__main__":
    app.run(debug=True)
