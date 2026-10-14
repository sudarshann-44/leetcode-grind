# Problem : https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=problem-list-v2&envId=array

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        write = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[write]:
                write+=1
                nums[write] = nums[i]
        return write + 1


solution = Solution()
print(solution.removeDuplicates([0,0,1,1,1,1,2,2,3,3,4]))