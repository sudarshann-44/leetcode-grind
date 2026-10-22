# https://leetcode.com/problems/set-mismatch/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii
class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        hashmap = {key: 0 for key in range(1, len(nums) + 1)}
        ans1 = []
        ans2 = []
        for element in nums:
           hashmap[element] =  hashmap.get(element, 0) + 1
        print(hashmap)
        for items in hashmap.items():
            if items[1] == 2:
                ans1.append(items[0])
            if items[1] == 0:
                ans2.append(items[0])
        return ans1 + ans2