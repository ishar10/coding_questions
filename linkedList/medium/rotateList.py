'''
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None or k ==0:
            return head
        curr = head
        l = 0
        while(curr):
            l+=1
            curr = curr.next
        while(k > l):
            k = k%l
        pos = l -k
        curr = head
        tmp = curr
        if pos ==0:
            return head
        while(pos):
            tmp = curr
            curr = curr.next
            pos-=1
        if curr:
            print(curr.val)
            while(curr.next):
                curr = curr.next
            curr.next = head
            head = tmp.next
            tmp.next = None
        return head