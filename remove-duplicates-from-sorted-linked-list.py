# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math
class Solution:

    def getData(self, head: ListNode, val: int):
        result = False
        temp_node = head
        while temp_node.next != None:
            if temp_node.val == val:
                result = True
            else:
                temp_node = temp_node.next
        return result
        

    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        temp_node = head
        while temp_node.next != None:
            if self.getData(head, temp_node.next.val): 
                temp_node.next = temp_node.next.next
            temp_node = temp_node.next

        return head



