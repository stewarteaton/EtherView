from flask import Flask, render_template
import config, ccxt
from web3 import Web3
import ccxt


app = Flask(__name__)

w3 = Web3(Web3.HTTPProvider(config.INFURA_URL))

@app.route("/")
def index():
    # connect to binance api
    binance = ccxt.binance()
    ether_price = binance.fetch_ticker('ETH/USDC')

    return render_template('index.html', ether_price=ether_price)

@app.route("/address/<addy>")
def address(addy):
    return render_template('address.html', addy=addy)

@app.route("/block/<blockNumber>")
def block(blockNumber):
    return render_template('transaction.html', blockNumber=blockNumber)

@app.route("/tx/<hash>")
def transaction(hash):
    transaction = w3.eth.get_transaction(hash)
    return render_template('transaction.html', hash=hash, transaction=transaction)