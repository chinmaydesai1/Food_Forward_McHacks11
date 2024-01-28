from flask import Blueprint, request, jsonify
import db
import json

foodBlueprint = Blueprint('food', __name__)

@foodBlueprint.route('/donateData/logIn', methods = ["POST", "GET"])
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

def updateFood(food_db, food_item):
    existing_item = food_db.find_one({"item": food_item['key']})
    if existing_item:
        food_db.update_one({"item": food_item['key']}, {"$inc": {"quantity": food_item['value']}})
    else:
        food_db.insert_one({"item": food_item['key'], "quantity": food_item['value']})

@foodBlueprint.route('/donateData', methods = ["POST", "GET"])
def retrieveFood():
    university = request.args.get('university')

    food_db = getFoodCollection(university)

    if not food_db:
        return jsonify({"status": False, "error": "Invalid university name"}), 400

    try:
        food_items = list(food_db.find({}, {"_id": 0}))
        return jsonify({"status": True, "data": food_items}), 200
    except Exception as e:
        return jsonify({"status": False, "error": str(e)}), 500

def getFoodCollection(university):
    if university == 'Concordia University':
        return db.db.ConcordiaFood
    elif university == 'McGill University':
        return db.db.McGillFood
    elif university == 'Université de Montréal':
        return db.db.UDMFood
    elif university == 'Polytechnique Montréal':
        return db.db.PolyFood
    else:
        return None
