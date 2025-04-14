from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/responder', methods=['POST'])
def responder():
    user_input = request.form['user_input']
    resposta = get_response(user_input)
    return jsonify({'resposta': resposta})

if __name__ == '__main__':
    app.run(debug=True)