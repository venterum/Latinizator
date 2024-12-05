from flask import Flask, request, jsonify, render_template
from latinizator import latinizator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text', '')
    translated_text = latinizator(text)
    return jsonify({'translated': translated_text})

if __name__ == "__main__":
    app.run(debug=True)