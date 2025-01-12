from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        map = {}
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
    
        print("check map", map)

        arr = []
        
        freq = [[] for i in range(len(nums) + 1)]

        for _ in nums:
            arr.append([])

        print("check arr", arr)
    
        print("check freq", freq)

        # print("Check map.item()", map.items())

        for num, cnt in map.items():
            arr[cnt-1].append(num)

        print("check final arr" ,arr)

        i = len(nums)-1

        print("check final i" ,i)

        res = []

        while i >= 0:
            if arr[i]:
                for num in arr[i]:
                    print("Check num", num)
                    res.append(num)
                    if len(res) == k:
                        return res
                    
            print("check i : ",i)
            i-=1

if __name__ == "__main__":
    # nums = [1,1,1,2,2,3]
    # k = 2
    
    nums = [1]
    k = 1 
    
    print(Solution().topKFrequent(nums, k))

            


        
        
        