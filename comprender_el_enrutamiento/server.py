from flask import Flask
app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "¡Hola Mundo!"

@app.route("/dojo")
def dojo():
    return "¡Dojo!"

@app.route("/say/<nombre>")
def say(nombre):
    return f"¡Hola, {nombre.capitalize()}!"

@app.route("/repeat/<int:num>/<string:nombre>")
def reapeat(num,nombre):
    return (num*nombre)

if __name__=="__main__":
    app.run(debug=True)