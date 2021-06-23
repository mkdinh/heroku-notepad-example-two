from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
from os import environ
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')
app.config['MONGO_URI'] = environ.get('MONGODB_URI')

# database setup
db = SQLAlchemy(app)
mongo = PyMongo(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)

@app.route('/')
def index():
    return 'My first API is live!'

@app.route('/api/notes/postgres')
def note_postgres():
    notes = db.session.query(Note)
    data = []

    for note in notes:
        data.append({
            "id": note.id,
            "content": note.content
        })

    return jsonify(data)


@app.route('/api/notes/mongo')
def note_mongo():
    notes = mongo.db.notes.find()
    data = []

    for note in notes:
        data.append({
            '_id': str(note['_id']),
            'content': note['content']
        })

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)