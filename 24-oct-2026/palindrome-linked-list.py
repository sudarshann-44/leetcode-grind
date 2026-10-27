# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if head is None:
            return False
        data = []
        current = head
        while current:
            data.append(str(current.val))
            current = current.next  
        
        return "".join(data) == "".join(data[::-1]) 