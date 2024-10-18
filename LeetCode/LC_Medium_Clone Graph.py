from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        neighbor_vals = [neighbor.val for neighbor in self.neighbors]  # Get the values of neighbors
        return f"Node(val={self.val}, neighbors={neighbor_vals})"


class Solution:

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        print("check node", node)
        