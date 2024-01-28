from flask import Blueprint, request, jsonify
from pymongo import MongoClient
import bcrypt

studentBlueprint = Blueprint('student', __name__)

client = MongoClient('mongodb+srv://Mchacks11:M2AeX5ZPGFgjQ7sn@mchacksjacd.kxfgecd.mongodb.net/')
db = client.McHacks11

@studentBlueprint.route('/studentFormData', methods = ["POST", "GET"])

def registerUser():
    data = request.json
    
    if db.Student.find_one({"email": data["email"]}):
        return jsonify({"status": False, "error": "Email already exists"}), 409

    hashedPassword = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    data['password'] = hashedPassword

    try:
        db.Student.insert_one(data)
        return jsonify({"status": True}), 201
    except Exception as e:
        return jsonify({"status": False, "error": str(e)}), 500
    
def getUserInfo():
    email = request.args.get('email')

    if not email:
        return jsonify({"status": False, "error": "Email parameter is missing"}), 400

    student_info = db.Student.find_one({"email": email}, {"_id": 0, "password": 0})

    if student_info:
        return jsonify({"status": True, "data": student_info}), 200
    else:
        return jsonify({"status": False, "error": "No student found with that email"}), 404
