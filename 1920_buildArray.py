from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i, v in enumerate(nums):
            nums[i] += n * (nums[nums[i]] % n)
        for i in range(0, n):
            nums[i] = nums[i] // n
        return nums


# Example usage
sol = Solution()
nums = [0,2,1,5,3,4]
print(sol.buildArray(nums))  # Example output: 3

