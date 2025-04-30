from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1 represents the maximum amount that can be robbed up to the previous house (i-2)
        # rob2 represents the maximum amount that can be robbed up to the current previous house (i-1)
        rob1, rob2 = 0, 0

        print(f"--- Starting rob function ---")
        print(f"Initial values: rob1 = {rob1}, rob2 = {rob2}")
        print("-" * 20)

        # Iterate through each house (represented by the amount 'num')
        for i, num in enumerate(nums):
            print(f"Processing house {i} with amount: {num}")

            # 'temp' calculates the maximum amount if we rob the current house.
            # This is the current house's amount ('num') plus the maximum amount robbed up to house (i-2) ('rob1').
            # We compare this with the maximum amount robbed up to house (i-1) ('rob2'),
            # which represents the case where we don't rob the current house.
            temp = max(num + rob1, rob2)
            print(f"  Calculation: temp = max(current_num + rob1, rob2) = max({num} + {rob1}, {rob2}) = {temp}")


            # Update rob1 to be the maximum amount robbed up to the previous house (i-1).
            # This was previously stored in rob2.
            rob1 = rob2
            print(f"  Updating rob1: rob1 becomes the previous rob2 = {rob1}")

            # Update rob2 to be the maximum amount robbed up to the current house (i).
            # This is the maximum of robbing the current house or not robbing it, which we calculated as 'temp'.
            rob2 = temp
            print(f"  Updating rob2: rob2 becomes temp = {rob2}")

            print(f"  End of iteration {i}: rob1 = {rob1}, rob2 = {rob2}")
            print("-" * 20)

        # After iterating through all houses, rob2 holds the maximum amount that can be robbed
        # from the entire row of houses.
        print(f"--- End of rob function ---")
        print(f"Final result (maximum amount robbed): {rob2}")
        return rob2

# Example usage:
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()
    # Call the rob method with an example list of house amounts
    result = solution.rob([1, 2, 3, 1])
    print(f"\nResult of robbing [1, 2, 3, 1]: {result}")

    # print("\n" + "="*30 + "\n")

    # # Another example
    # result_2 = solution.rob([2, 7, 9, 3, 1])
    # print(f"\nResult of robbing [2, 7, 9, 3, 1]: {result_2}")

