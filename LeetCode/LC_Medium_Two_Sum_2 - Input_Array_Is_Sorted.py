class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) -1

        # print("check l", l, "r", r) 

        for i in range(len(numbers)):
            # print("check 1", i)
            if numbers[l] + numbers[r] > target:
                r-=1
            elif numbers[l] + numbers[r] < target:
                l+=1
            elif numbers[l] + numbers[r] == target:
                return [l+1, r+1]
         

        # for i in range(len(numbers) - 1, -1, -1): 
            # print("check", i, "value:", numbers[i])