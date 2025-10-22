# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()

#         for i, a in enumerate(nums):

#             if a > 0:
#                 break

#             if i > 0 and a == nums[i - 1]:
#                 continue

#             l, r = i + 1, len(nums) - 1
#             while l < r:
#                 threeSum = a + nums[l] + nums[r]
#                 if threeSum > 0:
#                     r -= 1
#                 elif threeSum < 0:
#                     l += 1
#                 else:
#                     res.append([a, nums[l], nums[r]])
#                     l += 1
#                     r -= 1
#                     while nums[l] == nums[l - 1] and l < r:
#                         l += 1   
#         return res

# 2nd trial

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        print("Check nums", nums)

        for i, a in enumerate(nums):

            # print("check i =",i," a =", a)

            if a > 0:
                break

            if i > 0 and a == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1

            print("check l =",l, " r =", r)

            while l > r:
                sum = a + nums[l] + nums[r]
                if sum > 0:
                    r-=1
                elif sum < 0:
                    l+=1 


# 3rd
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res_Arr = []

        for i, a in enumerate(nums):

            if a > 0:
                break

            if i > 0 and a == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1

            while l < r:
                sum = a + nums[l] + nums[r]
        
                if sum > 0:
                    r-=1
                elif sum < 0:
                    l+=1
                else:
                    res_Arr.append([a,nums[l],nums[r]])
                    # print("check sum =", sum)
                    r-=1
                    l+=1
                    # print("check a =",a,"l =",l,"r =", r)
                    while nums[l] == nums[l-1] and l < r:
                        l+=1

        return res_Arr
                    
                    
                         


        