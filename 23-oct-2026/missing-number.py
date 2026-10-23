# Problem : https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        ranger = [i for i in range(len(nums) + 1)]
        for i in nums:
            if i in ranger:
                ranger.remove(i)
        return ranger[0]



hello = set([1, 2, 4])
hello2 = set([ 4, 5])

print(hello.intersection(hello2))