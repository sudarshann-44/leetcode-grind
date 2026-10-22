# Problem : https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/submissions/2178649934/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i == j:
                    pass
                else:
                    if nums[j] < nums[i]:
                        count += 1
            ans.append(count)
        return ans



nums =[60,14,3,39,49,43,53,24,33,13,32,93,65,26,77,55,2,28,2,50,18,4,92,20,57,90,64,86,54,69,28,80,88,66,57,28,67,83,3,50,86]
sol = Solution()
print(sol.smallerNumbersThanCurrent(nums))
# sol.smallerNumbersThanCurrent(nums)