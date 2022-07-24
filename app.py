import backend
# importing flask
from flask import Flask
from flask import render_template
from flask import request

from flask import Flask, redirect, url_for, request

# Importing the summarizer
from sentence_transformers import SentenceTransformer, util

# Using an instance of SBERT to create the model
# model = SBertSummarizer('paraphrase-MiniLM-L6-v2')

app = Flask(__name__)

# @app.route("/")
# def msg():
#     return render_template('index.html')
#
# @app.route("/getSummary", methods=['POST','GET'])
# def getSummary():
#     body=request.form['data']
#     result = model(body, num_sentences=5)
#     return render_template('evaluation.html',result=result)


@app.route("/")
def msg():
    return render_template('index.html')


@app.route('/evaluate', methods = ['POST', 'GET'])
def process():
    model = SentenceTransformer('all-MiniLM-L6-v2')

    if request.method == 'POST':
        text1 = request.form['text1']
        text2 = request.form['text2']

        text1 = list(text1)
        text2 = list(text2)

        # Compute embedding for both lists
        embeddings1 = model.encode(text1, convert_to_tensor=True)
        embeddings2 = model.encode(text2, convert_to_tensor=True)

        # Compute cosine-similarities
        cosine_scores = util.cos_sim(embeddings1, embeddings2)
        value = cosine_scores[0][0]
        result = 'Similarity Score of two Sentences is {}'.format(value)

        return redirect(url_for('evaluation', value = value))
    else:
        # user = request.args.get('name')
        text1 = request.args.get('text1')
        text2 = request.args.get('text2')

        text1 = list(text1)
        text2 = list(text2)

        # Compute embedding for both lists
        embeddings1 = model.encode(text1, convert_to_tensor=True)
        embeddings2 = model.encode(text2, convert_to_tensor=True)

        # Compute cosine-similarities
        cosine_scores = util.cos_sim(embeddings1, embeddings2)
        value = cosine_scores[0][0]
        result = 'Similarity Score of two Sentences is {}'.format(value)
        return render_template('evaluation.html', result = result)


if __name__ == "__main__":
    app.run(debug=True, port=8887)