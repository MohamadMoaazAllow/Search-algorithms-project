import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances


graph = {
    'A': {'B': 20, 'C': 20, 'D': 20, 'E': 20},
    'B': {'A': 20, 'F': 50 , 'G': 80},
    'F': {'B': 50, 'H': 80},
    'G': {'B': 80, 'H': 60},
    'H': {'F': 80, 'G': 80, 'I': 80},
    'C': {'A': 20, 'I': 40, 'J': 30, 'K': 55},
    'I': {'C': 40, 'H': 80, 'J': 20},
    'J': {'I': 20, 'C': 30, 'P': 20},
    'K': {'C': 55},
    'D': {'A': 20, 'L': 80, 'M': 100, 'N': 60},
    'L': {'D': 80},
    'M': {'D': 100},
    'N': {'D': 60},
    'E': {'A': 20, 'O': 20},
    'O': {'E': 20, 'P': 20, 'Q': 20},
    'Q': {'O': 20},
    'P': {'J': 20, 'O': 20}
}

start = 'A'
goal = 'P'
distances = dijkstra(graph, start)

shortest_path = []
current_node = goal
while current_node != start:
    shortest_path.append(current_node)
    current_node = min(graph[current_node], key=lambda x: distances[x])

shortest_path.append(start)
shortest_path.reverse()

print("Shortest path from node", start, "to node", goal + ":", shortest_path)
