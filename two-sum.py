

class Solution:

    def __init__(self):
        pass

    def two_sum(self, arr, target):
        hashmap = {}
        for i in range(0, len(arr)):
            compliment = target - arr[i]
            if compliment in hashmap:
                return [i, hashmap[compliment]]
            hashmap[arr[i]] = i



solution = Solution()

print(solution.two_sum([8, 5, 4, 15, 12, 7, 2], 11))