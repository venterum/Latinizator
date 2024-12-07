from flask import Flask, request, jsonify, render_template
import socket

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
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f'Latinizator доступен по адресу: {local_ip}:5000')
    app.run(debug=True, host=local_ip)