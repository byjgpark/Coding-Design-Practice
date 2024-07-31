class Heap: 
    def __init__(self):
        self.heap = []
        
    def insert(self, key):
        self.heap.append(key)
        self.heaplify_up(len(self.heap)-1)
        
    def heaplify_up(self, index):
        parent_index = (index - 1) // 2 
        
        while parent_index >= 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index
            parent_index = (index -1) // 2
    
    def is_empty(self):
        if not self.heap:
            return 
        
    def get_minValue(self):
        if self.is_empty():
            return 
        return self.heap[0] 
    
    def remove_minValue(self):
        if self.is_empty():
            return 
        
        #1 remove the min element
        #2 swap the last element with the first element 
        #3 bubbling down the element
        last_value = self.heap[-1]
        self.heap[0] = self.heap[-1]
        self.heaplify_down(0)
        
        
        print("find last index ", self.heap[-1])
        
    def heaplify_down(self, index):
        
        parent_index = (index - 1) // 2
        left_index = (parent_index * 2) + 1
        right_index = (parent_index * 2) + 2
        
        print("check here len :", len(self.heap))

        if len(self.heap) >= index and self.heap[left_index] < self.heap[index]:
            self.heap[index], self.heap[left_index] = self.heap[left_index], self.heap[index]
            # index = 
              
            

if __name__=="__main__": 
    heap = Heap()
    
    # heap.is_empty()
    heap.insert(3)
    heap.insert(2)
    heap.insert(15)
    heap.insert(5)
    heap.insert(4)
    heap.insert(45)

    print("check self.heap", heap.heap)
    
    print("check heaplify_down ", heap.heaplify_down(0))
    
    print("get min_value", heap.get_minValue())
    
    print("get min_value", heap.remove_minValue())
    
    # print("hey check here")