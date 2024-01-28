from flask import Blueprint, request, jsonify
from pymongo import MongoClient
import bcrypt
import db

businessBlueprint = Blueprint('business', __name__)

# client = MongoClient('mongodb+srv://Mchacks11:M3AeX5ZPGFgjQ7sn@mchacksjacd.kxfgecd.mongodb.net/')
# db = client.McHacks11

@businessBlueprint.route('/businessFormData', methods = ["POST", "GET"])
def registerUser():
    data = request.json
    
    # find_one() args - always check for "email" duplicates
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
    if not email:
        return jsonify({"status": False, "error": "Email parameter is missing"}), 400
    if not businessName:
        return jsonify({"status": False, "error": "Business Name parameter is missing"}), 400
    else:
        businessName = request.args.get('businessName')
    business_info = db.Business.find_one({"email": email}, {"_id": 0, "password": 0})
    address = request.args.get('address')
    contactNumber = request.args.get('contactNumber')
    passward = request.args.get('passward')

    if business_info & address != None & contactNumber != None & passward != None:
        return jsonify({"status": True, "data": business_info}), 200
    else:
        return jsonify({"status": False, "error": "No Business found with that email"}), 404
