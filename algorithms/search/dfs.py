# Implement the deep first search algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

# Implement dfs without recursion
def dfs_stack(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

# Example
graph = {'A': set(['B', 'C']), 'B': set(['A', 'D', 'E']), 'C': set(['A', 'F']), 'D': set(['B']), 'E': set(['B', 'F']), 'F': set(['C', 'E'])}
print("DFS:")
dfs(graph, 'A')
print("DFS without recursion:")
dfs_stack(graph, 'A')

# Implement the breadth first search algorithm
def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

# Example
print("BFS:")
bfs(graph, 'A')
