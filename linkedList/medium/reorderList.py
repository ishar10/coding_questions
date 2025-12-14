'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next == None:
            return head
        if head.next.next == None:
            return head
        one = head
        two = head.next
        curr = head
        l = 0
        while(curr):
            l+=1
            curr = curr.next
        l = l-2
        while(l>0):
            count = l
            temp = two
            while(count):
                count -=1
                two = two.next
            one.next = two
            one = temp
            two.next = one
            two = temp.next
            
            l = l-2
        if l <0:
            one.next = None
        else:
            two.next = None