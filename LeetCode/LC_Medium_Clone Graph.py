from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def print_node_info(node):
            if not node:
                print("Node is None")
                return
            neighbor_vals = [n.val for n in node.neighbors]
            print(f"Node value: {node.val}, Neighbors: {neighbor_vals}")

        def print_graph(start_node):
            if not start_node:
                print("Graph is empty")
                return
            visited = set()
            queue = [start_node]
            while queue:
                current = queue.pop(0)
                if current.val not in visited:
                    print_node_info(current)
                    visited.add(current.val)
                    queue.extend(current.neighbors)

        print("Original graph:")
        print_graph(node)

        # # Actual graph cloning logic
        # if not node:
        #     return None

        # clones = {}

        # def dfs(node):
        #     if node.val in clones:
        #         return clones[node.val]

        #     clone = Node(node.val)
        #     clones[node.val] = clone

        #     for neighbor in node.neighbors:
        #         clone.neighbors.append(dfs(neighbor))

        #     return clone

        # cloned = dfs(node)

        # print("\nCloned graph:")
        # print_graph(cloned)

        # return cloned