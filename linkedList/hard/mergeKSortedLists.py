'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def sort(head1,head2):
            l = ListNode()
            final = l
            while(head1 and head2):
                if head1.val <= head2.val:
                    l.next = head1
                    head1 = head1.next
                    l = l.next
                    l.next = None
                else:
                    l.next = head2
                    head2 = head2.next
                    l = l.next
                    l.next = None
            if head1:
                l.next = head1
            if head2:
                l.next = head2
            return final.next
        def merge(ll):
            if len(ll) == 1:
                return ll[0]
            elif len(ll) == 2:
                return sort(ll[0],ll[1])
            else:
                return sort(merge(ll[0:(len(ll)//2)+1]), merge(ll[(len(ll)//2)+1::]))
        if lists ==[]:
            l = ListNode()
            return l.next
        if len(lists) ==1:
            return lists[0]
        return merge(lists)
        # return sort(lists[0],lists[1])

        

                    



            

        