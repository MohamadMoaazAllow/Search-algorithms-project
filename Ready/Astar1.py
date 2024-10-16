import heapq

# تعريف الـ Heuristic الثابت لكل عقدة
static_heuristic = {
    'A': 60,
    'B': 80,    
    'C': 50,
    'E': 40,
    'D': 80,
    'F': 130,
    'G': 160,
    'I': 40,
    'H': 100,
    'J': 20,
    'K': 105,
    'L': 180,
    'M': 180,
    'N': 140,
    'O': 20,
    'Q': 40,
    'P': 0,
}

def astar(graph, start, goal):
    open_list = [(0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = g_score[start] + static_heuristic[start]
    nodes_expanded = 0
    
    while open_list:
        current_distance, current_node = heapq.heappop(open_list)
        nodes_expanded += 1  
        
        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            return path[::-1], nodes_expanded
        
        for neighbor, weight in graph[current_node].items():
            temp_g_score = g_score[current_node] + weight
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = g_score[neighbor] + static_heuristic[neighbor]
                heapq.heappush(open_list, (f_score[neighbor], neighbor))
    
    return None, nodes_expanded

# تعريف الرسم البياني (الجراف)
graph = {
    'A': {'B': 20, 'C': 20, 'D': 20, 'E': 20},
    'B': {'A': 20, 'F': 50, 'G': 80},
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

start_astar = 'A'
goal = 'P'
path, nodes_expanded = astar(graph, start_astar, goal)
print(f"Shortest path from node {start_astar} to node {goal}: {path}")
print(f"Number of expanded nodes: {nodes_expanded}")
