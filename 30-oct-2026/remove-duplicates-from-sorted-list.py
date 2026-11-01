# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Problem : https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-101)
        tail = dummy
        current = head
        while current:
            if tail.val != current.val:
                tempNode = ListNode(current.val, None)
                tail.next = tempNode
                tail = tail.next
            current = current.next
        return dummy.next