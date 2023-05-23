from flask import Flask, render_template, jsonify
from backend.blockchain.blockchain import Blockchain


app = Flask(__name__,template_folder='template')
blockchain = Blockchain()

@app.route('/')
def default():
    return render_template('index.html')


@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())


@app.route('/blockchain/mine')
def route_mine():
    transaction_data = 'transact_info'

    blockchain.add_block(transaction_data)

    return jsonify(blockchain.chain[-1].to_json())


app.run(debug=True)
