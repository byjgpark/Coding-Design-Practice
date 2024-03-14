class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1


        print("check l", l, "check r", r)

        print("check 1/2", 1//2)

        while l <= r:
            m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            # m = (l + r) // 2
            print("2nd check m", m)
            # if nums[2] = 3 > 0
            if nums[m] > target:
                # l = 0, r = 5, m = 2
                r = m - 1
                # r = 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

        