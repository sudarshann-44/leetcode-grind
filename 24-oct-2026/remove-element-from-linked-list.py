# problem : https://leetcode.com/problems/remove-linked-list-elements/


""" Using dummy node helps here because test case might involve removing head as well"""

class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        if head is None:
            return None
        dummy = ListNode(-1, head)
        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next 
        
        return dummy.next