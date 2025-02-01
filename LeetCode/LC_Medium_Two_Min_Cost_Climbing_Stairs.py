from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def dfs(i, depth=0):
            indent = '  ' * depth
            print(f"{indent}> dfs({i})")
            if i >= len(cost):
                print(f"{indent}< dfs({i}) returns 0")
                return 0
            
            res1 = dfs(i + 1, depth + 1)
            res2 = dfs(i + 2, depth + 1)
            result = cost[i] + min(res1, res2)
            print(f"{indent}< dfs({i}) returns {result} = {cost[i]} + min({res1}, {res2})")
            return result
        
        print("Calculating dfs(0):")
        result0 = dfs(0)
        print("\nCalculating dfs(1):")
        result1 = dfs(1)
        final_result = min(result0, result1)
        print(f"\nFinal result: min({result0}, {result1}) = {final_result}")
        return final_result

if __name__ == "__main__":
    cost = [10, 15, 20]
    print(Solution().minCostClimbingStairs(cost))