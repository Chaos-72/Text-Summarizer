import os

from transformers import pipeline
from bs4 import BeautifulSoup
import requests

# Create flask app
from flask import Flask, request, jsonify, render_template

summarizer = pipeline('summarization', model='sshleifer/distilbart-cnn-12-6')

app = Flask(__name__)

@app.route('/')
def home():
    # return "Welcome to the summarization API! Use the /summarize endpoint to get summaries."
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():

  data = request.get_json()
  url = data.get('url', '')
  min_length = int(data.get('min_length', 120))
  max_length = int(data.get('max_length', 30))


  # Fetch the parse content from hte URL
  r = requests.get(url)
  soup = BeautifulSoup(r.text, 'html.parser')
  result = soup.find_all(['h1', 'p'])
  text = ' '.join([res.text for res in result])

  # Split text into chunks for summarization

  print("Hello, World!")

  # text.replace('.', '.<eos>')
  # text.replace('?', '?<eos>')
  # text.replace('!', '!<eos>')
  # OR we can write it in this form
  text.replace('.', '.<eos>').replace('?', '?<eos>').replace('!', '!<eos>')
  sentences = text.split('<eos>')

  max_chunk = 500
  current_chunk = 0
  chunks = []

  for sentence in sentences:
    if len(chunks) == current_chunk + 1:
      if len(chunks[current_chunk]) + len(sentence.split('')) <= max_chunk:
        chunks[current_chunk].extend(sentence.split(' '))
      else:
        current_chunk += 1
        chunks.append(sentence.split(' '))

    else:
      chunks.append(sentence.split(' '))

  chunks = [' '.join(chunk) for chunk in chunks]

  # Summarize each chunk and join the summary
  summaries = summarizer(chunks, max_length=max_length, min_length=min_length, do_sample=False)
  final_summary = ' '.join([summ['summary_text'] for summ in summaries])

  print("End, World!")

  return jsonify({'original_text':chunks, 'summary': final_summary})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
