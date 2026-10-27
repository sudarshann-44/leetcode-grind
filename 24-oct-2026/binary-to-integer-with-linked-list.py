# Problem : https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        value = ""
        if head is None:
            return None
        current = head
        while current:
            value += str(current.val)
            current = current.next
        return int(value, 2)