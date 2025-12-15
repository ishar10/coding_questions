'''
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 


'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        leftNode = head
        rightNode = head
        curr = head
        tmp = curr
        left_dup = left
        if left == 1:
            tmp = None
        while(left-1):
            tmp = curr
            curr = curr.next
            left -=1

        leftToLeft = tmp
        leftNode = curr
        curr = head
        while(right-1):
            curr = curr.next
            right-=1
        rightNode = curr
        rightToRight = rightNode.next

        prev = None
        curr = leftNode
        while(curr!=rightToRight):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        if leftToLeft!= None:
            leftToLeft.next = rightNode
        leftNode.next = rightToRight
        if left_dup !=1:
            return head
        else:
            return rightNode

        