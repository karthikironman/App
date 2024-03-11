from flask import Flask, abort, jsonify, request, render_template
import joblib
# from feature import *
import json
#import pickle



def text_process(text):
    # Implement your text preprocessing logic here
    # This could include tokenization, stemming, stopword removal, etc.
    # For demonstration purposes, let's just return the input text as is
    return text


# # Open the file in binary read mode ('rb')
# with open('pipeline.sav', 'rb') as file:
#     # Load the pipeline object using pickle.load
#     pipeline = pickle.load(file)

pipeline = joblib.load('pipeline.sav')
# print(pipeline)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api',methods=['POST'])
def get_delay():

    result=request.form
    query_review = result['review']
    print(query_review)
    pred = pipeline.predict([query_review])
    print(pred)
    dic = {'CG':'Computer Generated Review','OR':'Original Review'}
    # return f'<html><body><h1>{dic[pred[0]]}</h1> <form action="/"> <button type="submit">back </button> </form></body></html>'
    '<html><body><h1>{}</h1> <form action="/"> <button type="submit">back </button> </form></body></html>'.format(dic[pred[0]])
    return 'test'


if __name__ == '__main__':
    app.run(port=8081, debug=True)
