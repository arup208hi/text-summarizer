from flask import Flask, request, render_template
from spacy_summarizer import text_summarizer
from nltk_summarizer import summarizer
app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        text = request.form['text']
        nltk_summary = summarizer(text)
        spacy_summary = text_summarizer(text)
    return render_template('index.html', text=text, nltk_summary=nltk_summary, spacy_summary=spacy_summary)
    
    
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")