from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from Student import studentBlueprint
import db

app = Flask(__name__)
CORS(app)
db.initialize_db()
app.register_blueprint(studentBlueprint, url_prefix='/student')

