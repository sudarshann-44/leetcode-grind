# problem : https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/
# Level Medium

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        if len(nums) == 0:
            return head

        nums = set(nums)

        dummy = ListNode(0, head)
        current = dummy

        while current.next:
            if current.next.val in nums:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next