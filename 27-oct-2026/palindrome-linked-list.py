# problem : https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if head is None:
            return False
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reversed_head = self.reverse_linked_list(slow) 
        first = head

        while reversed_head:
            if reversed_head.val != first.val:
                return False
            first = first.next
            reversed_head = reversed_head.next
        return True


    def reverse_linked_list(self, head: ListNode):

        prev = None
        current_node = head

        while current_node:
            nxt = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = nxt
        
        return prev
