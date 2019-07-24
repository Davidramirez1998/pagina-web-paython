from flask import Flask, redirect, url_for
app = Flask(__name__)

#El @ es un decorador.
@app.route ('/admin')
def hello_admin():
    return "Hello admin"


@app.route ('/invitado/<name>')
def hello_guest(name):
    return "Hello guest %s" % name

#nuevo enrutamiento.
@app.route ('/user/<name>')
def hello(name):
    if name == 'admin':
        return redirect (url_for('hello_admin'))
    else:
        return redirect (url_for('hello_guest', name = name))


if __name__ == '__main__':
    app.run (debug = True)




