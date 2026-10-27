# Problem : https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# defeats 100% yeahhhh

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(-1, head)
        fast = dummy 
        slow = dummy 

        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next 

        slow.next = slow.next.next

        return dummy.next