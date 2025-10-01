from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "API Flask funcionando "

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"mensagem": "Olá, mundo!"})

if __name__ == '__main__':
    app.run(debug=True)
