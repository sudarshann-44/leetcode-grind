# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Problem : https://leetcode.com/problems/merge-two-sorted-lists/
# beats 100% yeahh

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        
        # Create dummy node because head can be empty
        dummy = ListNode()

        # if both heads are empty return None
        if not list1 and not list2:
            return list1

        # start with dummy
        tail = dummy

        # while both lists are available
        while list1 and list2:

            # if first val is greater or equal add it to tail and move ahead
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next

            # if second val is greater or equal add it to tail and move ahead
            else:
                tail.next = list2
                list2 = list2.next

            # if equal move tail it self
            tail = tail.next

        # if both lists are of different size attach rest of them which ever is available
        tail.next = list1 if list1 else list2

        # return starting node
        return dummy.next