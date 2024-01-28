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
students = [f'Student{i}' for i in range(10)]
businesses = [f'Restaurant{i}' for i in range(5)]

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
pos = nx.spring_layout(G)  # Positioning of nodes
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()

#######################

# Positioning of nodes for better visualization
pos = nx.spring_layout(G, k=0.15, iterations=20)

# Separate colors for students and businesses
color_map = ['skyblue' if G.nodes[node]['type'] == 'student' else 'lightgreen' for node in G]

# Draw the graph
nx.draw(G, pos, with_labels=True, node_color=color_map, edge_color='gray', font_size=8)

# Optionally, draw edge weights as well
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)

# Display the plot
plt.show()
