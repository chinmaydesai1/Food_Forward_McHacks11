import sqlite3
import pandas as pd
from faker import Faker

faker = Faker()

# Generate fake data for 500 restaurants
restaurants_data = {
    "name": [faker.company() for _ in range(500)],
    "address": [faker.address() for _ in range(500)],
    "sponsors": [faker.company() for _ in range(500)],
    # Add more fields if needed
}

# Generate fake data for 500 students
students_data = {
    "contact_number": [faker.phone_number() for _ in range(500)],
    "password": [faker.password() for _ in range(500)],
    "self_photo": [faker.image_url() for _ in range(500)],
    # Add more fields if needed
}

restaurants_df = pd.DataFrame(restaurants_data)
students_df = pd.DataFrame(students_data)

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('montreal_db.sqlite')
cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS restaurants (
        id INTEGER PRIMARY KEY,
        name TEXT,
        address TEXT,
        sponsors TEXT
        -- Add more fields if needed
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        contact_number TEXT,
        password TEXT,
        self_photo TEXT
        -- Add more fields if needed
    )
''')

conn.commit()

restaurants_df.to_sql('restaurants', conn, if_exists='append', index=False)
students_df.to_sql('students', conn, if_exists='append', index=False)

conn.close()