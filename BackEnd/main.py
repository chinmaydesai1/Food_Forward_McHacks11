from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import re

app = Flask(__name__)
CORS(app)


client = MongoClient('mongodb+srv://Mchacks11:M2AeX5ZPGFgjQ7sn@mchacksjacd.kxfgecd.mongodb.net/')
db = client.McHacks11
