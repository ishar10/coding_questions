'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while(fast!= None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next
        prev = None
        while(slow!=None):
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        while(prev!=None and head!=None):
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True