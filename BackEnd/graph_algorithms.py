# -*- coding: utf-8 -*-
"""dummy-data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10tbC3gCQh7DZ4ioPGmdWMTTUrhZkP4qK
"""

!pip install faker

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

import sqlite3
import pandas as pd

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

# graph algorithms

import heapq
import random
import networkx as nx
import matplotlib.pyplot as plt

# Modified graph structure to include food availability and capacity
graph = {
    'business1': {'available_food': True, 'capacity': 10, 'students': 0, 'connections': {'school1': 7, 'school2': 2}},
    'business2': {'available_food': True, 'capacity': 8, 'students': 0, 'connections': {'school1': 3, 'school2': 4}},
    'school1': {'connections': {'business1': 7, 'school2': 6, 'business2': 3}},
    'school2': {'connections': {'business1': 2, 'school1': 6, 'business2': 4}},
}

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node]['connections'].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

def find_route(graph, start, locations):
    current_location = start
    route = [start]
    total_distance = 0

    while locations:
        distances = dijkstra(graph, current_location)

        # Filter locations based on constraints
        valid_locations = {
            loc for loc in locations
            if graph[loc].get('available_food', True) and graph[loc].get('students', 0) < graph[loc].get('capacity', float('infinity'))
        }

        if not valid_locations:
            break  # No valid locations left

        # Find the nearest valid location
        nearest = min(valid_locations, key=lambda loc: distances[loc])
        locations.remove(nearest)
        route.append(nearest)
        total_distance += distances[nearest]

        # Update student count for businesses
        if 'students' in graph[nearest]:
            graph[nearest]['students'] += 1

        current_location = nearest

    # Return to start
    distances = dijkstra(graph, current_location)
    total_distance += distances[start]
    route.append(start)

    return route, total_distance

# Locations to visit (excluding the start/end point)
locations = {'school1', 'school2'}
route, total_distance = find_route(graph, 'business1', locations)

print(f"Route: {route}")
print(f"Total Distance: {total_distance}")



# Example data - replace with your actual data
students = [f'Student{i}' for i in range(30)]
businesses = [f'Restaurant{i}' for i in range(6)]

# Function to mock suitability score (replace with your actual logic)
def calculate_suitability(student, business):
    # Your logic here. For now, returning a random score.
    return round(random.uniform(0.1, 1.0), 2)

# Example of creating a graph
G = nx.Graph()

# Adding nodes
for student in students:
    G.add_node(student, type='student')
for business in businesses:
    G.add_node(business, type='business')

# Adding edges with calculated suitability scores
for student in students:
    for business in businesses:
        weight = calculate_suitability(student, business)
        G.add_edge(student, business, weight=weight)

# Add more edges based on your criteria

# Plotting
pos = nx.spring_layout(G, k=0.5, iterations=20)  # Positioning of nodes
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()

#######################

# Positioning of nodes for better visualization
''' choose one of the presentation schemes '''
pos1 = nx.spring_layout(G, k=0.15, iterations=20)
pos2 = nx.circular_layout(G)
pos3 = nx.random_layout(G)
shells = [students, businesses]
pos4 = nx.shell_layout(G, shells)
pos = [pos1, pos2, pos3, pos4]

#######################

# Separate colors for students and businesses
color_map = ['skyblue' if G.nodes[node]['type'] == 'student' else 'lightgreen' for node in G]

# Draw the graph
for p in pos:
    nx.draw(G, p, with_labels=True, node_color=color_map, edge_color='gray', font_size=12)
    # Optionally, draw edge weights as well
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, p, edge_labels=edge_labels, font_size=6)
    # Display the plot
    plt.show()

# Max Flow / Min-Cut with NetworkX
def create_flow_network(G, students, businesses):
    ''' For the max flow problem, we can model the graph such that
    businesses and students are nodes, and edges represent the possibility
    of a student visiting a business. The capacity of each edge can
    represent the suitability score. '''

    F = nx.DiGraph()

    # Create source and sink nodes
    F.add_node("source")
    F.add_node("sink")

    # Add edges from source to students and from businesses to sink
    for student in students:
        F.add_edge("source", student, capacity=1)
    for business in businesses:
        F.add_edge(business, "sink", capacity=2)  # Assuming each business can accept 2 students

    # Add edges from students to businesses based on suitability
    for u, v, data in G.edges(data=True):
        if G.nodes[u]['type'] == 'student' and G.nodes[v]['type'] == 'business':
            F.add_edge(u, v, capacity=1, weight=data['weight'])

    return F

flow_network = create_flow_network(G, students, businesses)
flow_value, flow_dict = nx.maximum_flow(flow_network, 'source', 'sink')

''' why flow algorithm? '''

# Visualizing the graph with flow values
pos = nx.spring_layout(flow_network, k=0.15, iterations=20)

node_color = ['red' if node in ['source', 'sink'] else 'green' for node in flow_network]
node_size = [1000 if node in ['source', 'sink'] else 300 for node in flow_network]

edge_width = [2 * flow_network[u][v]['capacity'] for u, v in flow_network.edges()]

nx.draw(flow_network, pos, with_labels=True, node_color=node_color, node_size=node_size, width=edge_width)
plt.show()

import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('montreal_db.sqlite')

# Retrieve data into pandas DataFrames
restaurants_df = pd.read_sql_query("SELECT * FROM restaurants", conn)
students_df = pd.read_sql_query("SELECT * FROM students", conn)

conn.close()

import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes for restaurants
for _, row in restaurants_df.iterrows():
    G.add_node(row['businessName'], type='restaurant', cuisineType=row['cuisineType'], rating=row['rating'], seatingCapacity=row['seatingCapacity'])

# Add nodes for students
for _, student_row in students_df.iterrows():
    G.add_node(student_row['email'], type='student', school=student_row['school'])

    # Example: Adding edges based on a simple criterion, such as same cuisine preference
    for _, restaurant in restaurants_df.iterrows():
        G.add_edge(student_row['email'], restaurant['businessName'], weight=1)  # Weight could be a more complex function

if not nx.is_connected(G):
    print("The graph is not connected.")

# Example: Find the shortest path from a student to a restaurant
path = nx.dijkstra_path(G, source=students_df['email'][100], target=restaurants_df['businessName'][0])
print("Recommended best option:", path)

# Assuming each student has a demand of 1 and each restaurant a supply of 'seatingCapacity'
F = nx.DiGraph()
for student in students_df['email']:
    F.add_edge('source', student, capacity=1)
for _, restaurant in restaurants_df.iterrows():
    F.add_edge(restaurant['businessName'], 'sink', capacity=restaurant['seatingCapacity'])
    for student in students_df['email']:
        F.add_edge(student, restaurant['businessName'], capacity=1)  # Assuming every student is okay with every restaurant for simplicity

flow_value, flow_dict = nx.maximum_flow(F, 'source', 'sink')
print("Max flow:", flow_value)

import matplotlib.pyplot as plt

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=50)
nx.draw_networkx_edges(G, pos, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=8)
plt.show()

'''
To write a function that takes a student as a starting point, a list of
constraints, and outputs the optimal school for a food donation, we need to
define what "optimal" means in this context. Let's assume it's based on the
shortest path that meets the specified constraints, such as:
Food availability
Seating capacity
Distance
Given these assumptions, we can modify the find_route function to focus on
finding a single school that meets these constraints. Additionally, we will
use Pyplot to highlight the optimal path on the graph.
'''
'''

def find_optimal_school(graph, start_student, constraints):
    """
    Find the optimal school based on constraints.

    Args:
    graph (dict): The graph data structure.
    start_student (str): The starting student.
    constraints (dict): The constraints such as food availability, seating capacity, etc.

    Returns:
    str: The optimal school, None if no valid school is found.
    """
    optimal_school = None
    min_distance = float('infinity')

    start_student = ''
    student_mail = 'tiffanyward@concordia.ca'
    for _, stu in students_df.iterrows():
        if stu['email'] == student_mail:
            start_student = stu
            break

    # Run Dijkstra's algorithm from the starting student
    distances = dijkstra(graph, start_student)

    # Filter schools based on constraints
    for node, properties in graph.items():
        if properties.get('available_food', False) and properties.get('students', 0) < properties.get('capacity', 0):
            if node in distances and distances[node] < min_distance:
                min_distance = distances[node]
                optimal_school = node

    return optimal_school, min_distance

constraints = {
    'available_food': True,
    'capacity': 5  # Example capacity constraint
}

optimal_school, distance = find_optimal_school(graph, start_student, constraints)
print(f"Optimal school for 'student1' is {optimal_school} at a distance of {distance}")

# Compute the path using Dijkstra's algorithm
path = nx.dijkstra_path(G, source='student1', target=optimal_school)

# Plotting the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)

# Highlight the path
path_edges = list(zip(path, path[1:]))
nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='red')
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

plt.show()

'''