## chatgpt explaination link : https://chatgpt.com/c/68b77ff5-ddd8-8332-93e9-6e6f1cc47bf3

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        res = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1
        return res


# 2nd trial 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        hash_map = defaultdict(int)
        res = []
        
        for num in nums:
            hash_map[num]+=1

        for i in range(len(nums)):
            # print("check i", i)
            hash_map[nums[i]]-=1

            if i and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, len(nums)):
                hash_map[nums[j]]-=1
                target = -(nums[i]+ nums[j])

                if target > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i+1, len(nums)):         
                hash_map[nums[j]]+=1
        
        return res
        
        # print("check hash_map", hash_map)
        
        # print("check nums", nums)

        






        





        # nums.sort()  # [-4, -1, -1, 0, 1, 2]
 