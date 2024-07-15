import math

class HeapClass:
    def __init__(self):
        self.heap = []
        
    def insert(self, key):
        self.heap.append(key)
        
    def heaplifyUp(self, index):
        parent_index = math.floor(((index)-1)/2)
        while parent_index >=0 and self.heap[index] > self.heap[parent_index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            
        
        print("check Int :",((3-1)/2))
        
        # while
        # [1,2,3,4,5]
        # parentIndex = 

if __name__ == "__main__":
    
    heap = HeapClass()
    
    arr = [2,3,4,5,1]
    
    # print("check index ", arr[1.5])
    
    print("check here ", math.floor((2-1)/2))
    
    # heap.heaplifyUp()