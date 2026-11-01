# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def traverse_list(head: ListNode):
#         current_node = head
#         while current_node:
#             print(current_node.val)
#             current_node = current_node.next


# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

# # traverse_list(head)

# print([1, 2, 3, 4])

# Problem https://leetcode.com/problems/swap-nodes-in-pairs/
# beats 100% yeah 

class Solution:
    def swapPairs(self, head):
         if not head:
              return None
         if not head.next:
              return head
         current_node = head
         prev = None
         while current_node.next:
              next_node = current_node.next
              current_node.next = next_node.next
              next_node.next = current_node
              if prev:               
                  prev.next = next_node
              else:
                   prev = next_node
                   head = prev
              if current_node.next:
                prev = current_node
                current_node = current_node.next
         return head
    
sol = Solution()
# traverse_list(sol.swapPairs(None))
traverse_list(sol.swapPairs(head))