# Definition for singly-linked list.
'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]

Explanation:



Example 2:

Input: head = []

Output: []

Example 3:

Input: head = [1]

Output: [1]

Example 4:

Input: head = [1,2,3]

Output: [2,1,3]


'''
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        if head.next == None:
            return head
        prev = head
        curr = head.next
        temp = curr
        while(curr and prev):
            tmp = curr.next
            curr.next = prev
            if tmp!= None:
                curr = tmp.next
            else:
                curr = None
            if curr !=None:
                prev.next = curr
                prev = tmp
            else:
                prev.next = tmp
        return temp
        