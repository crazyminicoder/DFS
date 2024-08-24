def DFS(graph, start):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        print(node, end=' ')
        if node not in visited:
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    stack.append(neighbour)


graph = {
    'A': ['C', 'B'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

DFS(graph, 'A')
