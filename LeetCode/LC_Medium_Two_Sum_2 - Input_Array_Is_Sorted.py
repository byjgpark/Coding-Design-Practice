class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            # print("num :", i)
            for j in range(len(numbers)):
                print("check i", i,"j",j)
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]

        # for i in range(len(numbers) - 1, -1, -1): 
            # print("check", i, "value:", numbers[i])