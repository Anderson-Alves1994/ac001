
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

