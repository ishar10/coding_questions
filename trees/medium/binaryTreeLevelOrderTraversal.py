'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        final = []
        queue = [[0,root]]
        i = 0
        level = 1
        while(True):
            if i == 0:
                node = queue.pop(0)[1]
                final.append([node.val])
                i =1
                if node.left!= None:
                    queue.append([level,node.left])
                if node.right!= None:
                    queue.append([level,node.right])
                level+=1
            else:
                if queue == []:
                    return final
                else:
                    final.append([])
                    while(queue and queue[0][0]==(level-1)):
                        node = queue.pop(0)[1]
                        final[-1].append(node.val)
                        if node.left!= None:
                            queue.append([level,node.left])
                        if node.right!= None:
                            queue.append([level,node.right])
                    level+=1
        





        