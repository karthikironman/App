from flask import Flask, abort, jsonify, request, render_template
import joblib
# from feature import *
import json
import csv
#import pickle

def text_process(text):
    # Implement your text preprocessing logic here
    # This could include tokenization, stemming, stopword removal, etc.
    # For demonstration purposes, let's just return the input text as is
    return text

# pipeline = joblib.load('pipeline.sav')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


# @app.route('/raw_data')
# def display_data():
#     # Read the CSV file
#     csv_path = 'code/fake_reviews_dataset.csv'
#     df = pd.read_csv(csv_path)

#     # Convert DataFrame to HTML table
#     table_html = df.to_html(classes='table')

#     return render_template('rawData.html', table_html=table_html)


@app.route('/raw_data')
def display_data():
    # Read the CSV file using the csv module
    csv_path = 'code/fake_reviews_dataset.csv'
    with open(csv_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Read the header row
        data = list(reader)    # Read the remaining rows as data
        print(data)
    return render_template('rawData.html', header=header, data=data)

@app.route('/output')
def output():
    return render_template('output.html')


@app.route('/api', methods=['POST'])
def get_delay():
    result = request.form
    query_review = result['review']
    
    # Determine if the query review is CG or OR based on its length
    review_type = 'CG' if len(query_review) % 2 == 0 else 'OR'
    
    dic = {'CG': 'Computer Generated Review', 'OR': 'Original Review'}
    
    # Return the appropriate response
    return f'<html><body><h1>{dic[review_type]}</h1> <form action="/"> <button type="submit">back </button> </form></body></html>'


if __name__ == '__main__':
    app.run( host="0.0.0.0", port=8081, debug=True)
