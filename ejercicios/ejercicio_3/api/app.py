from flask import Flask
import os

app = Flask(__name__)

@app.route("/hola")
def hello():
    return "Hola " + os.environ["MI_NOMBRE"]


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8080)