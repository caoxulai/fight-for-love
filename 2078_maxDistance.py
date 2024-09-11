from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        max_distance = 0
        for i in range(0, n-1-max_distance):
            for j in range(n-1, i+max_distance, -1):
                if colors[i] != colors[j]:
                    max_distance = j - i
                    break  # Stop further iterations once the max distance is updated
        return max_distance


# Example usage
sol = Solution()
colors = [1, 2, 1, 6, 1, 1, 1]
print(sol.maxDistance(colors))  # Example output: 3

