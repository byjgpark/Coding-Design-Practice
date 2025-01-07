class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map = {}
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1

        print("check map", map.items())

        res = []
        for key, value in map.items():
            res.append((value,key))
        res.sort()

        ans = []
        while k > 0:
            
            ans.append(res.pop()[1])
            print("Check k", k)
            k-= 1
        
        return ans
        print("check res", ans)

        # for index, value in num
    


        
        