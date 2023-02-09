from flask import Flask, render_template, request
from machinetranslation import french_to_english, english_to_french

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/englishToFrench', methods=['POST'])
def translate_english_to_french():
    english_text = request.form['english_text']
    french_text = english_to_french(english_text)
    return french_text

@app.route('/frenchToEnglish', methods=['POST'])
def translate_french_to_english():
    french_text = request.form['french_text']
    english_text = french_to_english(french_text)
    return english_text

if __name__ == '__main__':
    app.run(debug=True)
