from flask import Flask, render_template
import config, ccxt, time
from web3 import Web3
import ccxt


app = Flask(__name__)

# Web3 using Infura API 
w3 = Web3(Web3.HTTPProvider(config.INFURA_URL))

def get_eth_price():
    # connect to binance api
    binance = ccxt.binance()
    ether_price = binance.fetch_ticker('ETH/USDC')    

    return ether_price

@app.route("/")
def index():

    eth = w3.eth
    ether_price = get_eth_price()

    latest_blocks = []
    for block_number in range(w3.eth.block_number, w3.eth.block_number-10, -1):
        block = w3.eth.get_block(block_number)
        latest_blocks.append(block)

    latest_transactions = []
    for tx in latest_blocks[-1]['transactions'][-10:]:
        transaction = w3.eth.get_transaction(tx)
        latest_transactions.append(transaction)

    current_time = time.time()

    return render_template('index.html', 
        eth = eth,
        ether_price=ether_price, 
        latest_blocks=latest_blocks, 
        latest_transactions=latest_transactions,
        current_time=current_time,
        miners = config.MINERS)

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