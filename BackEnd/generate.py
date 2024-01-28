import sqlite3
import pandas as pd
import random
from faker import Faker

faker = Faker()

cuisine_types = ['Italian', 'Chinese', 'American', 'Vegan', 'Indian', 'French', 'Mexican', 'Japanese', 'Thai', 'Mediterranean']
price_ranges = ['$', '$$', '$$$', '$$$$']
schools = ['Concordia University', 'McGill University', 'Université de Montréal', 'Polytechnique Montréal']

# Generate fake data for 500 restaurants
restaurants_data = {
    "businessName": [faker.company() for _ in range(500)],
    "contactNumber": ['514-' + faker.numerify(text='###-####') for _ in range(500)],  # Generate phone numbers with area code 514
    "address": [faker.address() for _ in range(500)],
    "sponsors": [faker.company() for _ in range(500)],
    "cuisineType": [random.choice(cuisine_types) for _ in range(500)],
    "rating": [round(random.uniform(1, 5), 1) for _ in range(500)],  # Ratings from 1 to 5
    "priceRange": [random.choice(price_ranges) for _ in range(500)],
    "seatingCapacity": [random.randint(10, 200) for _ in range(500)],  # Random seating capacity from 10 to 200
    "openingHours": [faker.time_object(end_datetime=None) for _ in range(500)]  # Generates random time objects
    # Add more fields if needed
}

email_domains = ['@mail.mcgill.ca', '@concordia.ca', '@umontreal.ca', '@polytechnique.ca']

# Generate fake data for 500 students
students_data = {
    "email": [faker.user_name() + random.choice(email_domains) for _ in range(500)],
    "contactNumber": ['514-' + faker.numerify(text='###-####') for _ in range(500)],
    "password": [faker.password() for _ in range(500)],
    "school": [random.choice(schools) for _ in range(500)]
    # Add more fields if needed
}

restaurants_df = pd.DataFrame(restaurants_data)
students_df = pd.DataFrame(students_data)

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('montreal_db.sqlite')
cursor = conn.cursor()

# Create tables
cursor.execute('DROP TABLE IF EXISTS restaurants')

# Then create the table with the updated CREATE TABLE statement
cursor.execute('''
    CREATE TABLE IF NOT EXISTS restaurants (
        id INTEGER PRIMARY KEY,
        businessName TEXT,
        contactNumber TEXT,
        address TEXT,
        sponsors TEXT,
        cuisineType TEXT,
        rating REAL,
        priceRange TEXT,
        seatingCapacity INTEGER,
        openingHours TEXT
    )
''')

cursor.execute('DROP TABLE IF EXISTS students')  # To reset the table if already exists

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        email TEXT,
        contactNumber TEXT,
        password TEXT,
        school TEXT
    )
''')

conn.commit()

restaurants_df.to_sql('restaurants', conn, if_exists='append', index=False)
students_df.to_sql('students', conn, if_exists='append', index=False)

conn.close()

# Connect to the SQLite database
conn = sqlite3.connect('montreal_db.sqlite')

# Query the database and load into pandas DataFrame
restaurants_df = pd.read_sql_query("SELECT * FROM restaurants", conn)
students_df = pd.read_sql_query("SELECT * FROM students", conn)

# Display the DataFrames
print(restaurants_df)
print(students_df)

# Close the connection
conn.close()