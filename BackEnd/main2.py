from flask import Flask, request, jsonify
from flask_cors import CORS
import bcrypt
import db
import json
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

app = Flask(__name__)
CORS(app)
db.initialize_db()

scheduler = BackgroundScheduler()

def reset_meal_and_snack():
    db.db.Student.update_many({}, {"$set": {"meal": {"meal": False}, "snack": 0}})

scheduler.add_job(func=reset_meal_and_snack, trigger="cron", hour=0, minute=0) #schedule reset
scheduler.start() #start scheduler
atexit.register(lambda: scheduler.shutdown()) #shut down when exiting app

@app.route('/studentFormData/logIn', methods=["POST", "GET"])
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

@app.route('/studentFormData', methods=["POST", "GET"])    
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

@app.route('/updateStudentFood', methods=["POST"])
def updateStudentFood():
    data = request.json

    student_email = data.get('email')
    university = data.get('university')
    meals = data.get('meals', {})  # Dictionary of meal items and their quantities
    snacks = data.get('snacks', {})  # Dictionary of snack items and their quantities

    try:
        student = db.db.Student.find_one({"email": student_email})
        if not student:
            return jsonify({"status": False, "error": "Student not found"}), 404

        #update student food data
        db.db.Student.update_one({"email": student_email}, {"$set": {"meal": {"meal": True}, "snack": len(snacks)}})

        #update university food data
        food_db = getFoodCollection(university)
        if not food_db:
            return jsonify({"status": False, "error": "Invalid university name"}), 400

        for meal, quantity in meals.items():
            updateFoodQuantity(food_db, meal, -quantity)
        for snack, quantity in snacks.items():
            updateFoodQuantity(food_db, snack, -quantity)

        return jsonify({"status": True, "message": "Student and food data updated successfully"}), 200

    except Exception as e:
        return jsonify({"status": False, "error": str(e)}), 500

def updateFoodQuantity(food_db, food_item, quantity_change):
    existing_item = food_db.find_one({"item": food_item})
    if existing_item:
        new_quantity = max(existing_item['quantity'] + quantity_change, 0) #to combat negative quantities
        food_db.update_one({"item": food_item}, {"$set": {"quantity": new_quantity}})
    else:
        pass

@app.route('/businessFormData/logIn', methods=["POST", "GET"])
def registerBusiness():
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

@app.route('/businessFormData', methods=["POST", "GET"])
def getBusinessInfo():
    email = request.json.get('email')
    password = request.json.get('password')

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

@app.route('/donateData/logIn', methods=["POST", "GET"])
def addFood(): 
    university = request.form.get('university')
    meals = json.loads(request.form.get('meals', '{}'))
    snacks = json.loads(request.form.get('snacks', '{}'))

    food_db = None
    if university == 'Concordia University':
        food_db = db.db.ConcordiaFood
    elif university == 'McGill University':
        food_db = db.db.McGillFood
    elif university == 'Université de Montréal':
        food_db = db.db.UDMFood
    elif university == 'Polytechnique Montréal':
        food_db = db.db.PolyFood

    if not food_db:
        return jsonify({"status": False, "error": "Invalid university name"}), 400

    try:
        for meal in meals:
            updateFood(food_db, meal)
        for snack in snacks:
            updateFood(food_db, snack)

        return jsonify({"status": True, "message": "Food data updated successfully"}), 200
    except Exception as e:
        return jsonify({"status": False, "error": str(e)}), 500
