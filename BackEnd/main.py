from flask import Flask
from flask_cors import CORS
import db
from student import studentBlueprint
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

app = Flask(__name__)
CORS(app)
db.initialize_db()
app.register_blueprint(studentBlueprint, url_prefix='/student')

scheduler = BackgroundScheduler()

def reset_meal_and_snack():
    db.db.Student.update_many({}, {"$set": {"meal": {"meal": False}, "snack": 0}})

scheduler.add_job(func=reset_meal_and_snack, trigger="cron", hour=0, minute=0) #schedule reset
scheduler.start() #start scheduler
atexit.register(lambda: scheduler.shutdown()) #shut down when exiting app


if __name__ == "__main__":
    app.run(debug=True)
