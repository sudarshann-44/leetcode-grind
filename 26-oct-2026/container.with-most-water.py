# Problem : https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left <= right:
            current_height = min(height[left], height[right])
            
            width = right - left

            max_water = max(max_water, width * current_height)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water