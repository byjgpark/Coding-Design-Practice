class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.k, self.nums = k, nums 

        heapq.heapify(self.nums)

        while len(self.nums) > self.k:
            heapq.heappop(self.nums)        

    def add(self, val: int) -> int:

        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]



        # return 3
        

# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4 [4,5,8,2,3]
# kthLargest.add(5);   // return 5 [4,5,8,2,3,5]
# kthLargest.add(10);  // return 5 [4,5,8,2,3,5,10]
# kthLargest.add(9);   // return 8 [4,5,8,2,3,5,10,9]
# kthLargest.add(4);   // return 8 [4,5,8,2,3,5,10,9,4]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)