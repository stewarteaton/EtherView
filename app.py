from flask import Flask, render_template
import config
from web3 import Web3

app = Flask(__name__)

w3 = Web3(Web3.HTTPProvider(config.INFURA_URL))

@app.route("/")
def index():
    return "<p>Ether View!</p>"

@app.route("/address/<addy>")
def address(addy):
    return render_template('address.html', addy=addy)

@app.route("/block/<blockNumber>")
def block(blockNumber):
    return render_template('transaction.html', blockNumber=blockNumber)

@app.route("/tx/<hash>")
def transaction(hash):
    return render_template('transaction.html', hash=hash)