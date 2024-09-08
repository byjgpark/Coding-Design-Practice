 class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # Print current state
            print(f"dfs called with i={i}, cur={cur}, total={total}")

            # If total matches the target, add to result
            if total == target:
                print(f"Found valid combination: {cur}")
                res.append(cur.copy())
                return

            # If total exceeds target or index is out of bounds, stop exploring this path
            if i >= len(candidates) or total > target:
                print(f"Exceeded target or no more candidates: cur={cur}, total={total}")
                return

            # Decision 1: Include the current candidate and explore further
            cur.append(candidates[i])
            print(f"Including {candidates[i]}, new cur={cur}, new total={total + candidates[i]}")
            dfs(i, cur, total + candidates[i])  # Recurse with current candidate

            # Backtrack by removing the last candidate and exploring the next option
            print(f"Backtracking, removing {cur[-1]} from cur={cur}")
            cur.pop()

            # Decision 2: Exclude the current candidate and move to the next
            dfs(i + 1, cur, total)  # Move to the next candidate

        dfs(0, [], 0)  # Initial call
        return res

if __name__ == "__main__":
    # Example usage:
    solution = Solution()
    nums = [1, 2]
    result = solution.subsets(nums)
    print(f"Final subsets: {result}")

