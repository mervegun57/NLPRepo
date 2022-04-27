from flask import Flask, request, jsonify
from models import deneme
from flask_cors import CORS
import spacy
from spacy import displacy
from spacy.lang.en.examples import sentences


app = Flask(__name__)
CORS(app)

deneme = deneme.Deneme()


@app.route('/ner/', methods=['GET'])
def get_tasks():
    return jsonify(deneme.ner()), 200


@app.route('/deneme/<string:deneme_id>/', methods=['GET'])
def get_task(deneme_id):
    return deneme.find_by_id(deneme_id), 200


@app.route('/deneme/', methods=['POST'])
def add_tasks():
    if request.method == "POST":
        title = request.form['title']
        body = request.form['body']
        response = deneme.create({'title': title, 'body': body})
        return response, 201


@app.route('/deneme/<string:deneme_id>/', methods=['PUT'])
def update_tasks(deneme_id):
    if request.method == "PUT":
        title = request.form['title']
        body = request.form['body']
        response = deneme.update(deneme_id, {'title': title, 'body': body})
        return response, 201


@app.route('/deneme/<string:deneme_id>/', methods=['DELETE'])
def delete_tasks(deneme_id):
    if request.method == "DELETE":
        deneme.delete(deneme_id)
        return "Record Deleted"


if __name__ == '__main__':
    app.run(debug=True)
