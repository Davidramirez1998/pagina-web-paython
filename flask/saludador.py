from flask import Flask
app = Flask(__name__)

#El @ es un decorador.
@app.route ('/hello/<name>')
def hello(name):
    print name
    return "Hello %s" % name

if __name__ == '__main__':
    app.run (debug = True)

#Para mostrar todo lo que se hace en la consola.
