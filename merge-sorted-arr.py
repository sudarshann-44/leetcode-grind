class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for i in nums2:
            if i != 0:
                nums1.append(i)
        nums1 = [i for i in nums1 if i != 0]
        nums1.sort()
sol = Solution()
sol.merge([1,2,3,0,0,0],6, [2,5,6], 3)