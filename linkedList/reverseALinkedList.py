'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''
#iteratively

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev

#recursively

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        def rev(prev,curr):
            if curr == None:
                return prev
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            return rev(prev,curr)
        return rev(prev,curr)
