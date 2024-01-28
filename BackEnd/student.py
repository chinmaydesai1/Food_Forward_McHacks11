from flask import Blueprint, request, jsonify
import bcrypt
import db

studentBlueprint = Blueprint('student', __name__)


@studentBlueprint.route('/studentFormData', methods=["POST", "GET"])
def registerUser():
    data = request.json

    hashedPassword = bcrypt.hashpw(
        data['password'].encode('utf-8'), bcrypt.gensalt())
    data['password'] = hashedPassword

    data['meal'] = {"meal": False}
    data['snack'] = 0

    try:
        db.Student.insert_one(data)
        return jsonify({"status": True}), 201
    except Exception as e:
        return jsonify({"status": False, "error": str(e)}), 500


@studentBlueprint.route('/studentFormData/logIn', methods=["POST", "GET"])
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


@studentBlueprint.route('/updateStudentFood', methods=["POST"])
def updateStudentFood():
    data = request.json

    student_email = data.get('email')
    university = data.get('university')
    # Dictionary of meal items and their quantities
    meals = data.get('meals', {})
    # Dictionary of snack items and their quantities
    snacks = data.get('snacks', {})

    try:
        student = db.db.Student.find_one({"email": student_email})
        if not student:
            return jsonify({"status": False, "error": "Student not found"}), 404

        # update student food data
        db.db.Student.update_one({"email": student_email}, {
                                 "$set": {"meal": {"meal": True}, "snack": len(snacks)}})

        # update university food data
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
        # to combat negative quantities
        new_quantity = max(existing_item['quantity'] + quantity_change, 0)
        food_db.update_one({"item": food_item}, {
                           "$set": {"quantity": new_quantity}})
    else:
        pass
