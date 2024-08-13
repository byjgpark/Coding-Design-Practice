
# 1. Brute-force way to solve this problem

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        arr = stones 

        while len(arr) > 1:

            arr.sort()
            last_stone = arr[-1] - arr[-2]
            arr.pop()
            arr.pop()
            arr.append(last_stone)
        
        return arr[0]


# 2. Using a heap to solve this problem

