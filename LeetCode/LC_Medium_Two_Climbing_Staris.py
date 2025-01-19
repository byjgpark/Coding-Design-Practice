class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(i, depth=0):
            indent = "  " * depth  # Create indentation for readability
            
            # Debug: Print entering the function
            print(f"{indent}dfs({i}) called.")
            
            # Base case
            if i >= n:
                result = int(i == n)
                # Debug: Print the base case result
                print(f"{indent}Base case reached at dfs({i}). Returning {result}.")
                return result
            
            # Debug: Print before making recursive calls
            print(f"{indent}Calling dfs({i + 1}) and dfs({i + 2}) from dfs({i}).")
            
            # Recursive calls
            left = dfs(i + 1, depth + 1)  # dfs for i + 1
            right = dfs(i + 2, depth + 1)  # dfs for i + 2
            
            # Debug: Print after recursive calls
            print(f"{indent}Results of dfs({i + 1}) = {left} and dfs({i + 2}) = {right}.")
            
            # Sum up the results
            result = left + right
            # Debug: Print the final result of this call
            print(f"{indent}Returning {result} from dfs({i}).")
            
            return result
        
        return dfs(0)

if __name__ == "__main__":
    n = 3
    print(f"Number of ways to climb {n} stairs: {Solution().climbStairs(n)}")
