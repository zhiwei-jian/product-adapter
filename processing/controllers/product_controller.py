from flask import Flask, jsonify, make_response
from processing.product import product

app = Flask(__name__)
print('=========' + __name__)

@app.route('/')
def hello_world():
    data = {
        "Modules": 15,
        "Subject": "Data Structures and Algorithms",
    }

    return jsonify(data)


@app.route('/product')
def getProduct():
    users = product.findUser()
    user = users[0]
    return jsonify(users)
    # return make_response(jsonify(users), 200)

def run():
    app.run(host='127.0.0.1', port=6000)
