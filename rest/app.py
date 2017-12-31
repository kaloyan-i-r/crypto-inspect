from flask import Flask,jsonify
import repackage
repackage.up()
from data import crud

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/tickers')
def tickers():
    return jsonify(crud.read_one('cms_tickers','latest'))


if __name__ == '__main__':
    tickers()