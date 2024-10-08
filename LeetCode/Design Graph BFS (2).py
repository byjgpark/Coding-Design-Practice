
from collections import deque

class Graph:    
    def __init__(self, graph, start):
        
        self.graph = graph
        self.start = start
        
    def bfs(self):
        visted = set()
        queue = deque([self.start])
        
        while queue:
            node = queue.popleft()
            # print("Check node :", node)
            if node not in visted:
                visted.add(node)
                print(node, end=" ")
                queue.extend(self.graph[node])
                
        # return visted

if __name__ == "__main__":    
    # Use the BFS function on a graph
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E'],
    }
    
    graph = Graph(graph, 'A')
    
    # print("checking graph", graph.bfs())
    
    graph.bfs()
    
    # https://medium.com/@sergioli/breath-first-and-depth-first-search-on-tree-and-graph-in-python-99fd1861893e

