from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        print("Initial cost array:", cost)
        # Loop from len(cost)-3 down to 0 (inclusive)
        for i in range(len(cost) - 3, -1, -1):
            print("\nProcessing index i =", i)
            print("Before update: cost =", cost)
            # Retrieve the next two costs
            next1 = cost[i + 1]
            next2 = cost[i + 2]
            chosen = min(next1, next2)
            
            print("cost[{}] = {}".format(i, cost[i]))
            print("cost[{}] = {}".format(i + 1, next1))
            print("cost[{}] = {}".format(i + 2, next2))
            print("Chosen minimum of next two steps:", chosen)
            
            # Update cost[i] with the chosen minimum
            cost[i] += chosen
            print("After update: cost[{}] becomes {}".format(i, cost[i]))
            print("Updated cost array:", cost)
            
        
        result = min(cost[0], cost[1])
        print("\nFinal updated cost array:", cost)
        print("Result: min(cost[0], cost[1]) = min({}, {}) = {}".format(cost[0], cost[1], result))
        return result

if __name__ == "__main__":
    solution = Solution()
    final_result = solution.minCostClimbingStairs([10, 15, 20])
    # final_result = solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
    # what is final_result's langth ?
    # what is [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]'s length ?   
    # print("check ", len([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  
    print("\nFinal result:", final_result)
