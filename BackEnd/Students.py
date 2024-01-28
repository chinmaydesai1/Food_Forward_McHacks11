from flask import Blueprint, request, jsonify
from pymongo import MongoClient
import bcrypt
import db

studentBlueprint = Blueprint('student', __name__)

@studentBlueprint.route('/studentFormData', methods = ["POST", "GET"])
def registerUser():
    data = request.json
    
    if db.Student.find_one({"email": data["email"]}):
        return jsonify({"status": False, "error": "Email already exists"}), 409

    hashedPassword = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    data['password'] = hashedPassword

    data['meal'] = {"meal": False}
    data['snack'] = 0 

    try:
        db.Student.insert_one(data)
        return jsonify({"status": True}), 201
    except Exception as e:
        return jsonify({"status": False, "error": str(e)}), 500

@studentBlueprint.route('/studentFormData', methods = ["POST", "GET"])    
def getUserInfo():
    email = request.json.get('email')
    password = request.json.get('password')

    if not email or not password:
        return jsonify({"status": False, "error": "Email and password are required"}), 400

    student_info = db.db.Student.find_one({"email": email})

    if student_info:
        if bcrypt.checkpw(password.encode('utf-8'), student_info['password']):
            student_info.pop('password', None)
            student_info.pop('_id', None)
            return jsonify({"status": True, "data": student_info}), 200
        else:
            return jsonify({"status": False, "error": "Invalid password"}), 401
    else:
        return jsonify({"status": False, "error": "No student found with that email"}), 404
