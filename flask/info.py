from flask import Flask
app = Flask(__name__)

#El @ es un decorador.
@app.route ('/entero/<int:valor>')
def entero(valor):
    return "Hello %d" % valor

#Flotante es un numero decimal.
@app.route ('/flotante/<float:valor>')
def flotante(valor):
    return "Hello %f" % valor

if __name__ == '__main__':
    app.run (debug = True)



#Para mostrar todo lo que se hace en la consola.
