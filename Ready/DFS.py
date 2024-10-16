def dfs_all_paths(graph, start, goal):
    all_paths = [] 
    stack = [(start, [start])]
    
    while stack:
        node, path = stack.pop()
        if node == goal: 
            all_paths.append(path)
        for neighbor in graph[node]:
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))
    
    return all_paths

def get_longest_path(all_paths):
    longest_path = None
    max_length = 0
    
    for path in all_paths:
        if len(path) > max_length:
            longest_path = path
            max_length = len(path)
    
    return longest_path


graph_dfs = {
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
start_dfs = 'A'
goal = 'P'

all_paths = dfs_all_paths(graph_dfs, start_dfs, goal)
longest_path = get_longest_path(all_paths)

# Print the longest path
print('path from A to P :',longest_path)