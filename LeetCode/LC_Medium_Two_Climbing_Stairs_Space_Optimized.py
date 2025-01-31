class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            print("check i", i)
            temp = one
            one = one + two
            two = temp
        
        return one
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(5))  