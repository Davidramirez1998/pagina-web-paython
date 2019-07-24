from flask import Flask
app = Flask(__name__)

#EL @ es un decorador.
@app.route ('/')
def hello ():
    return "Hello world in flask"


# en parentesis es lo que va en URL.
@app.route ('/dos')
def dos ():
    return "usted se encuentra en dos"

if __name__ == '__main__':
    app.run ()
