class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    
    def __str__(self):
        return f"Node(val={self.val}, neighbors={[n.val for n in self.neighbors]})"
    
    def __repr__(self):
        return self.__str__()

class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        # print("check node from the cloneGraph function", node)
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            # copying the value of the node
            copy = Node(node.val)
            print("check copy inside of the dfs function", copy)
            print("check oldToNew :", oldToNew)
            print("check node inside of the dfs function", node)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        print("check node from the cloneGraph function", node)
        return dfs(node) if node else None
    
    def createGraphFromAdjList(self, adjList):
        if not adjList:
            return None
        
        # Create all nodes
        # nodes = [Node(i+1) for i in range(len(adjList))]
        
        # Create all nodes
        nodes = []  # Initialize an empty list to store the nodes
        for i in range(len(adjList)):  # Iterate through the indices of the adjacency list
            node_value = i + 1  # Calculate the node value (1-indexed)
            new_node = Node(node_value)  # Create a new Node object with the calculated value
            nodes.append(new_node)  # Add the new node to the list of nodes

        # Add neighbors
        # for i, neighbors in enumerate(adjList):
        #     nodes[i].neighbors = [nodes[j-1] for j in neighbors]
        
        # Add neighbors
        for i, neighbors in enumerate(adjList):
            neighbor_nodes = []  # Create an empty list to store the neighbor nodes
            for j in neighbors:  # Iterate over each neighbor in  the neighbors list
                neighbor_nodes.append(nodes[j-1])  # Find the corresponding node and add it to the neighbor_nodes list
                print("check j", j)
                print("nodes[j-1]:", nodes[j-1])
            nodes[i].neighbors = neighbor_nodes  # Assign the list of neighbors to the current node
            print("neighbor_nodes:", neighbor_nodes)
        
        print("nodes inside of the createGraphFromAdjList function", nodes)
        
        return nodes[0]  # Return the first node as the entry point

    def printGraph(self, node):
        if not node:
            print("Empty graph")
            return
        visited = set()
        def dfs(node):
            if node.val in visited:
                return
            visited.add(node.val)
            for neighbor in node.neighbors:
                dfs(neighbor)
                
        dfs(node)

if __name__ == "__main__":
    solution = Solution()
    
    # Input adjacency list
    adjList = [[2,4],[1,3],[2,4],[1,3]]
    
    # Create and print the original graph
    original = solution.createGraphFromAdjList(adjList)
    print("Original Graph:")
    solution.printGraph(original)

    print("check original from the main function", original)
    # Clone the graph and print the clone
    cloned = solution.cloneGraph(original)
    print("\nCloned Graph:")
    solution.printGraph(cloned)
