#!flask/bin/python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields
# Create resource managers and endpoints
from flask_rest_jsonapi import Api, ResourceDetail, ResourceList


#------This script allows communinication between client and server------#

# Create a new Flask application
app = Flask(__name__)

# Set up SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///verse.db'
db = SQLAlchemy(app)
db.app = app

# Define a class for the Verse table
class Verse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emotion = db.Column(db.String)
    text = db.Column(db.String)
    reference = db.Column(db.String)
    version = db.Column(db.String)

# Create the table
db.create_all()

# Create data abstraction layer
class VerseSchema(Schema):
    class Meta:
        type_ = 'verse'
        self_view = 'verse_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'verse_many'

    id = fields.Integer()
    emotion = fields.Str(required=True)
    text = fields.Str(required=True)
    reference = fields.Str(required=True)
    version = fields.Str(required=True)

# Set up endpoint for interacting with one verse
class VerseMany(ResourceList):
    schema = VerseSchema
    data_layer = {'session': db.session,
                  'model': Verse}

# Set up endpoint for interacting with many verses
class VerseOne(ResourceDetail):
    schema = VerseSchema
    data_layer = {'session': db.session,
                  'model': Verse}

api = Api(app)
api.route(VerseMany, 'verse_many', '/verses')
api.route(VerseOne, 'verse_one', '/verses/<int:id>')

# main loop to run app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
   
