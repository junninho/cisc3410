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

visited = set() # keep track of visited nodes

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

def main():
    dfs(visited, graph, 'S')

main()