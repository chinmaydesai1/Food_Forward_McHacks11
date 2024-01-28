import heapq

def dijkstra(graph, start):
    # Initialize distances and priority queue
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example graph (distance matrix)
graph = {
    'business1': {'school1': 7, 'school2': 2},
    'school1': {'business1': 7, 'school2': 6, 'business2': 3},
    'school2': {'business1': 2, 'school1': 6, 'business2': 4},
    'business2': {'school1': 3, 'school2': 4}
}

def find_route(graph, start, locations):
    current_location = start
    route = [start]
    total_distance = 0

    while locations:
        distances = dijkstra(graph, current_location)
        # Find the nearest location
        nearest = min(locations, key=lambda loc: distances[loc])
        locations.remove(nearest)
        route.append(nearest)
        total_distance += distances[nearest]
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
