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

        # first_index = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        self.heaplify_down(self.heap, self.heap[0])
        
        return self.heap[0]
            
    def isEmpty(self):
        return len(self.heap)
        
            
    def heaplify_down(self, heap, index):
        
        print("check heap inside of heap function", heap)
        
        smallest = heap[0]
        left_child_index = ( 2 * index ) + 1 
        right_child_index = ( 2 * index ) + 2
        
        if left_child_index < len(heap) and heap[index] > heap[left_child_index]:
            smallest = left_child_index
            
        if right_child_index < len(heap) and heap[index] > heap[right_child_index]:
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
    
    print("check ", heap.getMinVal())
    
    print("check heap after heaplify_down ", heap.heap)


