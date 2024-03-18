class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # 1, find max num til k
        # 2, sliding windiw -> subtracking left pointer and adding right pointer from the sum
        # 3, find the max => find average 
          # Get sum for starting window
        _sum = sum(nums[:k])
        max_sum = _sum

        # Start sliding window
        start_index = 0
        end_index = k

        print("check end_index", end_index)
        print("check len(nums)", len(nums))
        while end_index < len(nums):

            print("check end_index", end_index)
            print("check len(nums)", len(nums))
            
            _sum -= nums[start_index]  # Remove previous element
            start_index += 1

            _sum += nums[end_index]  # Add next element
            end_index += 1

            print("Check _sum", _sum)
            print("Check max_sum", max_sum)
            max_sum = max(max_sum, _sum)  # Update max sum

        # Return the average
        return max_sum / k
        


           
            # break
            
            



        



       


       