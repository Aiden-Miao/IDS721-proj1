from flask import Flask
from flask import jsonify
from flask import redirect
app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World! this is IDS721 proj1. Aiden'

@app.route('/<name>')
def changename(name):
    """change the helloworld name"""
    newlink = "Hello World! this is IDS721 proj1. " + name
    return newlink

@app.route('/echo/<name>')
def echo(name):
    """shows newname: name on the page"""
    val = {"newname": name}
    return jsonify(val)

@app.route('/coursecalendar')
def coursecalendar():
    """leads to the course calendar page"""
    return redirect('https://noahgift.github.io/cloud-data-analysis-at-scale/calendar')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)