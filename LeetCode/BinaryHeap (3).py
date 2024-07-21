class Heap:
    def __init__(self):
        self.heap = []
        
    def insert(self, key):
        self.heap.append(key)
        self.heaplify_up(len(self.heap)-1)
        
    def heaplify_up(self, index):
        parent_index = ( (index - 1) // 2)
        while parent_index >= 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index
            parent_index = ( (index -1 ) // 2)
            
    def getMinVal(self):
        if self.isEmpty() == 0:
            return 
        # min_val = self.heap[0]
        # self.heap[0] = self.heap[-1]
        # self.heap.pop()
        
        # self.heaplify_down(self.heap, 0)
        
        return self.heap[0]
            
    def isEmpty(self):
        return len(self.heap)
    
    def deleteMinVal(self):
        if self.isEmpty() == 0:
            return 
        
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heaplify_down(self.heap, 0)
        return min_val
    
    def heaplify_down(self, heap, index):
        
        # print("check heap inside of heap function", heap)
        # print("Check index inside of heaplify_down", index)
        # smallest = 0
        smallest = index
        left_child_index = ( 2 * index ) + 1 
        right_child_index = ( 2 * index ) + 2
        # left_child_index -> 5 < 5 x
        if left_child_index < len(heap) and heap[smallest] > heap[left_child_index]:
            smallest = left_child_index
        # right_child_index -> 6 < 5 x
        if right_child_index < len(heap) and heap[smallest] > heap[right_child_index]:
            smallest = right_child_index
            
        if index != smallest:
            heap[index], heap[smallest] = heap[smallest], heap[index]
            self.heaplify_down(heap, smallest)

if __name__ == "__main__":

    heap = Heap()

    heap.insert(3)
    heap.insert(2)
    heap.insert(15)
    heap.insert(5)
    heap.insert(4)
    heap.insert(45)

    print("check heap arr ", heap.heap)
    
    print("What is a min-value :", heap.getMinVal())
    
    print("Deleted val :", heap.deleteMinVal())

    print("check heap after heaplify_down ", heap.heap)


