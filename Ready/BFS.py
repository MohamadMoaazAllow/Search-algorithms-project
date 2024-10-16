def bfs(graph, start, goal):
    visited = []
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            visited.append(node)
            if node == goal:
                return path
            else:
                adjacent_nodes = graph.get(node, [])
                for node2 in adjacent_nodes:
                    new_path = list(path)
                    new_path.append(node2)
                    queue.append(new_path)
    return None 

graph = {
    'A': ['B', 'C', 'D', 'E'],
    'B': ['A', 'F', 'G'],
    'F': ['B', 'H'],
    'G': ['B', 'H'],
    'H': ['F', 'G', 'I'],
    'C': ['A', 'I', 'J', 'K'],
    'I': ['C', 'H', 'J'],
    'J': ['I', 'C', 'P'],
    'K': ['C'],
    'D': ['A', 'L', 'M', 'N'],
    'L': ['D'],
    'M': ['D'],
    'N': ['D'],
    'E': ['A', 'O'],
    'O': ['E', 'P', 'Q'],
    'Q': ['O'],
    'P': ['J', 'O']
}

solution = bfs(graph, 'A', 'P')
print('path from A to P:', solution)