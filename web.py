from flask import Flask, request, jsonify, render_template
import socket
import unicodedata

from latinizator import latinizator

app = Flask(__name__)

def remove_diacritics(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text)
                  if not unicodedata.combining(c))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text', '')
    output_modes = data.get('output_modes', [])
    
    translated_text = latinizator(text)
    
    if 'uppercase' in output_modes:
        translated_text = translated_text.upper()
    elif 'lowercase' in output_modes:
        translated_text = translated_text.lower()
        
    if 'no_diacritics' in output_modes:
        translated_text = remove_diacritics(translated_text)
        
    return jsonify({'translated': translated_text})

if __name__ == "__main__":
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f'Latinizator доступен по адресу: {local_ip}:5000')
    app.run(debug=True, host=local_ip, port=5000)