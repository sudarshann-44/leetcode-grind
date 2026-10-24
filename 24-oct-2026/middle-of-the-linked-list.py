# problem : https://leetcode.com/problems/middle-of-the-linked-list/
#  Beats 100 % yeahhh...

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:

        if head is None:
            return None
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

        