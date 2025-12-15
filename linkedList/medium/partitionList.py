'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = head
        greater = head
        curr = head
        while(curr):
            if curr.val == x or curr.val >x:
                greater = curr
                break
            curr= curr.next
        if curr == None:
            return head
        curr = head
        while(curr):
            if curr.val < x:
                less = curr
                break
            curr= curr.next
        if curr == None:
            return head
        curr = head
        curr1 = less
        curr2 = greater
        while(curr):
            if curr.val < x and curr!= less:
                curr1.next = curr
                curr1 = curr
            elif (curr.val >x or curr.val ==x) and curr!=greater:
                curr2.next = curr
                curr2 = curr
            curr = curr.next
        curr2.next = None  
        curr1.next = greater
        return less



        
        