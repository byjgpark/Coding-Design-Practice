def DFS(graph, start):
    visited = set()  # keep track of the visited nodes
    stack = [start]  # use a stack to keep track of nodes to visit next
    step = 1

    print(f"Initial stack: {stack}")

    while stack:
        print(f"\nStep {step}:")
        print(f"Current stack: {stack}")
        
        node = stack.pop()  # get the next node to visit
        print(f"Popped node: {node}")
        
        if node not in visited:
            visited.add(node)  # mark the node as visited
            print(f"Visiting node: {node}")
            print(f"Visited set: {visited}")
            
            neighbors = graph[node]
            print(f"Neighbors of {node}: {neighbors}")
            
            stack.extend(neighbors)
            print(f"Stack after adding neighbors: {stack}")
        else:
            print(f"Node {node} already visited, skipping")
        
        step += 1

    print("\nDFS traversal complete")

# Use the DFS function on a graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

print("Graph structure:")
for node, neighbors in graph.items():
    print(f"{node}: {neighbors}")

print("\nStarting DFS traversal:")
DFS(graph, 'A')  # Output: A C F E B D