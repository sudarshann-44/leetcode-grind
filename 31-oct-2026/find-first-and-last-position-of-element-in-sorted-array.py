# Incomplete

class Solution(object):
    def searchRange(self, nums, target):
        start = 0
        end = len(nums) - 1
        ans = [-1, -1]
        while start <= end:
            print("start", start, end)
            mid = start + (end - start) // 2
            if nums[mid] == target:
                ans[0] = mid
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else: 
                start = mid + 1
        return ans
    
    def findFirst(nums, target):
        start = 
        end = len(nums) - 1

        while start <= end:
                    print("start", start, end)
                    mid = start + (end - start) // 2
                    print("c", mid)
                    if nums[mid] == target:
                        ans[0] = mid
                        end = mid - 1
                    elif nums[mid] > target:
                        end = mid - 1
                    else: 
                        start = mid + 1
                return ans


    def findLast(nums, target):
        start = 0
        end = len(nums)


# class Solution(object):
#     def searchRange(self, nums, target):
#         start = {i : -1 for i in nums}
#         end = {i : -1 for i in nums}
#         for i in range(len(nums)):
#             num = nums[i]
#             if start.get(num) == -1:
#                 start[num] = i
#             end[num] = i
#         return [start[target], end[target]]
    
sol = Solution()
print(sol.searchRange([5,7,7,8,8,10], 8))