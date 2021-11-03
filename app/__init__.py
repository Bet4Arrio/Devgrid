from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import configparser


app = Flask(__name__)
app.config.from_object('config')


db = SQLAlchemy(app)
ma = Marshmallow(app)
configParser = configparser.RawConfigParser()   
configFilePath = r'config.ini'
configParser.read(configFilePath)

API_KEY= configParser.get('credentials', 'api_key')
from .models import users, cities 
from .routes import routes

if __name__ == "__main__":
    app.run()