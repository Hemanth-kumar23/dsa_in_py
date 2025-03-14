# Graph representation as an adjacency list
graph = {
    'A': ['B', 'D', 'E', 'F'],
    'D': ['A'],
    'B': ['A', 'F', 'C'],
    'F': ['B', 'A'],
    'C': ['B'],
    'E': ['A']
}

print("Given Graph is:")
print(graph)

def dfs_traversal(input_graph, source):
    stack = []  # Stack for DFS
    visited_list = []  # List to track visited nodes

    stack.append(source)
    visited_list.append(source)

    while stack:
        vertex = stack.pop()  # Get the last inserted node (LIFO)
        print(vertex, end=" ")

        for u in input_graph[vertex]:
            if u not in visited_list:
                stack.append(u)
                visited_list.append(u)

print("\nDFS traversal of graph with source A is:")
dfs_traversal(graph, "A")
