from collections import Counter
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)

        pair = 0
        leftover = 0
        for num, count in counts.items():
            pair += count // 2  # Add pairs
            leftover += count % 2  # Add leftovers

        return [pair, leftover]


# Example usage
sol = Solution()
nums = [1, 3, 2, 1, 3, 2, 2]
print(sol.numberOfPairs(nums))  # Example output: [3, 1]
