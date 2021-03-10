# use dictionary to define graph structure

graph = {
    'S' : ['A', 'D'],
    'A' : ['D', 'B'],
    'B' : ['C', 'E'],
    'C' : [],
    'D' : ['E'],
    'E': ['B', 'F'],
    'F': ['G'],
    'G': []
}

visited = []

queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s)

        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

def main():
    bfs(visited, graph, 'S')

main()