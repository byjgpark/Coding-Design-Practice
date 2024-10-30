class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    
    def __str__(self):
        return f"Node(val={self.val}, neighbors={[n.val for n in self.neighbors]})"
    
    def __repr__(self):
        return self.__str__()

class Solution:
    # def cloneGraph(self, node: "Node") -> "Node":
    #     # print("check node from the cloneGraph function", node)
    #     oldToNew = {}
    #     def dfs(node):
    #         # print("check node inside of the dfs function :", node)
    #         if node in oldToNew:
    #             # print("oldToNew[node] :", oldToNew[node])
    #             return oldToNew[node]
            
    #         # copying the value of the node
    #         copy = Node(node.val)
    #         # print("check copy inside of the dfs function", copy)
    #         # print("check oldToNew :", oldToNew)
    #         # print("check node inside of the dfs function", node)
    #         oldToNew[node] = copy
    #         # print("check oldToNew[node] after the copy :", oldToNew)
    #         # print("check copy right before for loop:", copy)
            
    #         for nei in node.neighbors:
    #             # print("check nei inside of the for loop:", nei)
    #             copy.neighbors.append(dfs(nei))
            
    #         # print("check copy right after for loop:", copy)
    #         return copy
        
    #     # print("check node from the cloneGraph function", node)
    #     return dfs(node) if node else None
    
    def cloneGraph(self, node: "Node") -> "Node":
        print("\n=== Starting cloneGraph with node:", node)
        oldToNew = {}
        recursion_depth = 0  # To track DFS depth
        
        def dfs(node, depth):
            nonlocal recursion_depth
            recursion_depth = depth
            indent = "    " * depth  # Visual indentation for print clarity
            
            print(f"\n{indent}🔄 DFS Level {depth} called with node: {node}")
            print(f"{indent}Current oldToNew dictionary: {oldToNew}")
            
            # Check if node is already cloned
            if node in oldToNew:
                print(f"{indent}✓ Node {node.val} already exists in oldToNew")
                print(f"{indent}Returning existing copy: {oldToNew[node]}")
                return oldToNew[node]
            
            # Create new node copy
            copy = Node(node.val)
            print(f"{indent}📝 Created new copy node: {copy}")
            
            # Add to dictionary
            oldToNew[node] = copy
            print(f"{indent}📊 Updated oldToNew dictionary: {oldToNew}")
            
            # Process neighbors
            print(f"{indent}👥 Processing neighbors of node {node.val}: {[n.val for n in node.neighbors]}")
            
            for i, nei in enumerate(node.neighbors):
                print(f"\n{indent}⭐ Processing neighbor {i+1}/{len(node.neighbors)} of node {node.val}: {nei}")
                neighbor_copy = dfs(nei, depth + 1)
                copy.neighbors.append(neighbor_copy)
                print(f"{indent}➕ Added neighbor {neighbor_copy.val} to node {copy.val}'s neighbors")
                print(f"{indent}📋 Current neighbors of node {copy.val}: {[n.val for n in copy.neighbors]}")
            
            print(f"\n{indent}✅ Completed processing node {node.val}")
            print(f"{indent}Final state of copy node {copy.val}: {copy}")
            
            return copy
        
        # Handle empty graph case
        if not node:
            print("Empty graph received")
            return None
        
        # Start DFS
        result = dfs(node, 0)
        print("\n=== Final Result ===")
        print("Final oldToNew dictionary state:")
        # print("check oldToNew :", oldToNew)
        # print("check oldToNew.items() :", oldToNew.items())
        for original, copied in oldToNew.items():
            print("check original :", original, "copied :", copied)
            # print(f"Original {original.val} -> Copy {copied.val} with neighbors {[n.val for n in copied.neighbors]}")
        return result
        
        
        # My 1st attempt
        # if not node:
        #     return 
        # # 
        # old_neighbor = {}

        # # 
        # def dfs(node):
            
        #     print("check dfs function", node)
        #     if node in old_neighbor:
        #         # print("Check node[node.val]", node[node.val])
        #         return old_neighbor[node]
        #         # return node[node.val]


        #     copy = Node(node.val)
        #     print("Check copy", copy)
        #     old_neighbor[node] = copy
            
        #     print("Check old_neighbor[node]", old_neighbor)
            
        #     for nei in node.neighbors:
        #         print("check nei", nei)
        #         node.neighbors.append(dfs(nei))

        # if node:
        #     return dfs(node)
        # else:
        #     return 
        

    
    
    def createGraphFromAdjList(self, adjList):
        if not adjList:
            return None
        
        # Create all nodes
        nodes = [Node(i+1) for i in range(len(adjList))]
        

        print("check nodes inside of the createGraphFromAdjList function", nodes)
        
        # Create all nodes
        # nodes = []  # Initialize an empty list to store the nodes
        # for i in range(len(adjList)):  # Iterate through the indices of the adjacency list
        #     node_value = i + 1  # Calculate the node value (1-indexed)
        #     new_node = Node(node_value)  # Create a new Node object with the calculated value
        #     nodes.append(new_node)  # Add the new node to the list of nodes
        
        # print("*******nodes inside of the createGraphFromAdjList function", nodes)

        # Add neighbors
        # for i, neighbors in enumerate(adjList):
        #     nodes[i].neighbors = [nodes[j-1] for j in neighbors]
    
        # Add neighbors
        for i, neighbors in enumerate(adjList):
            # print("i :", i, "neighbors :", neighbors)
            neighbor_nodes = []  # Create an empty list to store the neighbor nodes
            for j in neighbors:  # Iterate over each neighbor in  the neighbors list
                print("nodes =", nodes)
                print("nodes[j-1] =", nodes[j-1])
                print("check j =", j)
                print("check j-1 =", j-1)
                neighbor_nodes.append(nodes[j-1])  # Find the corresponding node and add it to the neighbor_nodes list
                print("neighbor_nodes:", neighbor_nodes)
            nodes[i].neighbors = neighbor_nodes
            # print("nodes at the end of the for loop :", nodes)
            # Assign the list of neighbors to the current node
            # print("neighbor_nodes:", neighbor_nodes)
        
        # print("nodes inside of the createGraphFromAdjList function", nodes)
        
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
            print(f"Node {node.val}: neighbors = {[n.val for n in node.neighbors]}")
            for neighbor in node.neighbors:
                dfs(neighbor)
        dfs(node)

if __name__ == "__main__":
    solution = Solution()
    
    # Input adjacency list
    adjList = [[2,4],[1,3],[2,4],[1,3]]
    
    # Create and print the original graph
    original = solution.createGraphFromAdjList(adjList)
    
    print("check original from the main function", original)
    
    print("Original Graph:")
    solution.printGraph(original)

    # print("check original from the main function", original)
    # Clone the graph and print the clone
    cloned = solution.cloneGraph(original)
    print("\nCloned Graph:")
    solution.printGraph(cloned)


#Claude.ai
#https://claude.site/artifacts/4e8ba047-a127-4152-b80b-2ef150c0c5c6
