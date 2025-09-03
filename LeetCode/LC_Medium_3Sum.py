from typing import List

# working
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(tmp))
        print("check res =",res)
        return [list(i) for i in res]

if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))

## 2nd trial
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        Set = set()
        print("Check nums", nums)

        for i in range(1 ,len(nums)):
            # print("check i = ", i)
            for j in range(i+1 ,len(nums)):
                for k in range(j+1 ,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = []
                        print("check =", nums[i], nums[j], nums[k])

## 3rd trial
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = set()
        # print("Check nums", nums)

        for i in range(0 ,len(nums)):
            # print("check i = ", i)
            for j in range(i+1 ,len(nums)):
                for k in range(j+1 ,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(temp))
                        print("check =", nums[i], nums[j], nums[k])
                        # print("Check temp =", temp)
                        # print("Check tuple =", res)
        # [print("check =",i) for i in res]
        return [list(i) for i in res]
        # answer = []
        # for i in res:
        #     answer.append(list(i))
        #     # print("check i =", i)

        # return answer