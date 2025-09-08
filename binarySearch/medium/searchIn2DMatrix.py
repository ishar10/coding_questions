'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = [0,0]
        high = [0,len(matrix[0])-1]
        i =0
        while(True):
            x = low[0]
            y = low[1]
            x1 = high[0]
            y1 = high[1]
            if target > matrix[x1][y1]:
                if (x+1) == len(matrix):
                    return False
                else:
                    low[0] = x+1
                    low[1] =0
                    high[0] = x+1
                    high[1] = y1
            else:
                i = x
                break
        nums = matrix[i]
        l = 0
        r = len(nums)-1
        while(l<=r):
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        return False