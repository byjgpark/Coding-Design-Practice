class GraphClass:
    
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        
    
    def dfs(self):
        
        visited = set()
        stack = [self.start]
        
        # print("check graph", graph)
        
        # print("check start", start)
        
        while stack:
            node = stack.pop()
            
            if node not in visited:
                visited.add(node)
                print(node, end=" ")
                stack.extend(self.graph[node])

if __name__== "__main__":
    
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E'],
    }
    
    dfsGraph = GraphClass(graph, 'A')
    dfsGraph.dfs()