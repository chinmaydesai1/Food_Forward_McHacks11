from pymongo import MongoClient

db = None

def initialize_db():
    global db
    client = MongoClient('mongodb+srv://Mchacks11:M2AeX5ZPGFgjQ7sn@mchacksjacd.kxfgecd.mongodb.net/')
    db = client.McHacks11
