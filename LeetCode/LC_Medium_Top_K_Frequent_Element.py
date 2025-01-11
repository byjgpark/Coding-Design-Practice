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

        for _ in nums:
            arr.append([])

        print("check arr", arr)

        # print("Check map.item()", map.items())

        for num, cnt in map.items():
            arr[cnt-1].append(num)

        print("check final arr" ,arr)

        i = len(nums)-1

        print("check final i" ,i)

        res = []

        while i >= 0:
            print("check i", i)
            if arr[i]:
                for num in arr[i]:
                    print("Check num", num)
                    if num == k:
                        
            i-=1


        
        
        