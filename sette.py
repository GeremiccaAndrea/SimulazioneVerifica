from flask import Flask, render_template
app = Flask(__name__)

import datetime

@app.route('/') # L'utente richiede l'home page
def index():
  return render_template("index4.html", ora = datetime.datetime.now())

@app.route('/pippo')
def pippo():
    return('Pippo non esiste')

@app.route('/mappa/<width>')
def mappawidth(width):
    return render_template("index7.html", dimensione = width)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)