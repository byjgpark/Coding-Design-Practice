from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)
        
        print(f"Initial store: {store}")
        print(f"Initial res: {res}\n")
        
        for num in store:
            print(f"Current num: {num}")
            if num - 1 not in store:
                streak = 1
                curr = num + 1
                print(f"  Starting new sequence at {num}, streak: {streak}, curr: {curr}")
                
                while curr in store:
                    streak += 1
                    curr += 1
                    print(f"    Extended sequence: streak: {streak}, curr: {curr}")
                
                res = max(res, streak)
                print(f"  Updated res: {res}\n")
            else:
                print(f"  {num} is not the start of a sequence (since {num - 1} is in store)\n")
        
        print(f"Final res: {res}")
        return res

if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    sol = Solution()
    sol.longestConsecutive(nums)

# 1st trial
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        store = set(nums)
        res = 0

        # print("check sets =", sets)

        print("check length =", len(nums))

        for num in store:
            
            if num-1 not in store:

                curr = num + 1
                streak = 1

                while curr in store:

                    # print("check num in while", curr)
                    streak+=1
                    curr+=1
                    # res = max(res, streak)                    
                res = max(res, streak)
            # print("check num", num)
        return res


