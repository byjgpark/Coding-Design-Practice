class BinaryHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        
        # print("check index ", index, "something ", (6-1)// 2)
        print("check index ", index, "check parent_index", parent_index)
        
        while parent_index >= 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index
        
            parent_index = (index - 1) // 2
          
    def get_min(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def delete_min(self):
        if self.is_empty():
            return None
        
        # find min value 
        min_value = self.heap[0]
        
        # assign the last index at the first index
        self.heap[0] = self.heap[-1]
        # pop the duplicate value
        self.heap.pop()
        # heapify down the min value from the tree 
        self._heapify_down(0)

        return min_value

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)


# Example Usage
if __name__ == "__main__":
    
    heap = BinaryHeap()

    # Insert elements
    # heap.insert(3)
    # heap.insert(2)
    # heap.insert(15)
    # heap.insert(5)
    # heap.insert(4)
    # heap.insert(45)
    
    # Insert elements
    heap.insert(4)
    heap.insert(50)
    heap.insert(7)
    heap.insert(55)
    heap.insert(90)
    heap.insert(87)
    heap.insert(2)
    
    print("check init heap", heap.heap)

    print("Minimum element in the heap:", heap.get_min())

    # Delete minimum element
    print("Deleted minimum element:", heap.delete_min())
    
    print("after deleting heap.heap: ", heap.heap)
    # arr = [1,2,3,4]
    
    # arr.pop()

