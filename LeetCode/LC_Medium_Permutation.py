class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # print("check num", num)
        n = len(nums)
        res = []

        def backtrack(sol):
            
            # base case 
            if len(sol) == n:
                res.append(sol.copy())
                print("check sol", sol)
                return
            
            for x in nums:
                if x not in sol: 
                    sol.append(x)
                    backtrack(sol)
                    sol.pop()

            print("check nums", nums) 

        backtrack([])

        return res 