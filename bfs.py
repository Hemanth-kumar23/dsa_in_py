from queue import Queue

graph = {
    'A': ['B', 'D', 'E', 'F'],
    'D': ['A'],
    'B': ['A', 'F', 'C'],
    'F': ['B', 'A'],
    'C': ['B'],
    'E': ['A']
}

def BFS(graph, start):
    Q = Queue()
    visited = []

    Q.put(start)
    visited.append(start)

    while not Q.empty():
        node = Q.get()
        print(node, end=" ")

        for i in graph[node]:
            if i not in visited:
                Q.put(i)
                visited.append(i)

print("BFS Traversal:")
BFS(graph, 'A')
