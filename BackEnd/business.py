from flask import Blueprint, request, jsonify
import bcrypt
import db

businessBlueprint = Blueprint('business', __name__)

@businessBlueprint.route('/businessFormData', methods = ["POST", "GET"])
def registerUser():
    data = request.json
    
    if db.Business.find_one({"email": data["email"]}):
        return jsonify({"status": False, "error": "Email already exists"}), 409

    hashedPassword = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    data['password'] = hashedPassword

    if db.Business.find_one({"businessName": data["businessName"]}):
        return jsonify({"status": False, "error": "Business already exists"}), 409 
    
    try:
        db.Business.insert_one(data)
        return jsonify({"status": True}), 201
    except Exception as e:
        return jsonify({"status": False, "error": str(e)}), 500
    
@businessBlueprint.route('/businessFormData', methods = ["POST", "GET"])
def getUserInfo():
    email = request.args.get('email')
    password = request.args.get('password')

    if not email:
        return jsonify({"status": False, "error": "Email parameter is missing"}), 400
    if not password:
        return jsonify({"status": False, "error": "Password is missing"}), 400
    
    business_info = db.db.Business.find_one({"email": email})
    
    if business_info:
        if bcrypt.checkpw(password.encode('utf-8'), business_info['password']):
            business_info.pop('password', None)
            business_info.pop('_id', None)
            return jsonify({"status": True, "data": business_info}), 200
        else:
            return jsonify({"status": False, "error": "Invalid password"}), 401
    else:
        return jsonify({"status": False, "error": "No business found with that email"}), 404
