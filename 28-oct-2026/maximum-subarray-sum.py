# https://leetcode.com/problems/maximum-average-subarray-i/
# Concept of sliding window -> Don't calculate sum always just add and subtract leaving and joining elements

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        start = 0
        highest_sum = None
        previous_sum = None

        while (start + k) <= len(nums):
            end = start + k

            if previous_sum == None:
                sum1 = sum(nums[start: end])
                previous_sum = sum1
            else:
                sum1 = previous_sum - nums[start - 1] + nums[end - 1]
                previous_sum = sum1

            summation = float(sum1/ k)

            if highest_sum == None:
                highest_sum = summation
    
            if summation > highest_sum:
                highest_sum = summation
    
            start += 1
        return highest_sum