from flask import Flask,jsonify
import repackage,json
repackage.up()
from data import crud,cache
from gather import coinmarketcap as cmc

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, API World!'


@app.route('/global')
def global_data():
    data = cache_get("cmc_global",cmc.api.global_data)
    return jsonify(data)

@app.route('/tickers')
def tickers():
    # tickers = crud.read_one('cmc_ticker','latest')['data']
    tickers = cache_get("cmc_tickers",cmc.api.ticker)
    return jsonify(tickers)

def cache_get(key, getter):
    obj = cache.get(key)
    if obj is None:
        obj = getter()
        cache.set(key,json.dumps(obj))
    else:
        obj = json.loads(obj)
    return obj

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000, debug=True)