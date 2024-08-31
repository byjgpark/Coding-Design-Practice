class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = [] 
        
        def dfs(i):
            print(f"Entering dfs({i}), current subset: {subset}, res: {res}")
            if i >= len(nums):
                res.append(subset.copy())
                print(f"Base case reached, adding {subset.copy()} to res: {res}")
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            print(f"Including nums[{i}] = {nums[i]}, subset now: {subset}")
            # dfs(1), dfs(3)
            dfs(i + 1)  # Move to the next element
            
            # backtracking process
    
            print(f"Backtracking from dfs({i + 1}), current subset before pop: {subset}")
            subset.pop()  # Backtrack
            print(f"Excluding nums[{i}] = {nums[i]}, subset after pop: {subset}")
            
            # dfs(2)
            dfs(i + 1)  # Move to the next element without including current element
            print(f"This is the end of function")
            
        # Start the DFS with the first element
        dfs(0)
        return res

# Example usage:
solution = Solution()
nums = [1, 2, 3]
result = solution.subsets(nums)
print(f"Final subsets: {result}")
