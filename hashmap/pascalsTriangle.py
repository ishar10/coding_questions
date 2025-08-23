'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        final = [[1], [1,1]]
        temp = [1]
        count = 0
        while(count<(numRows-2)):
            i = 0
            j = i+1
            while(j<len(final[-1])):
                temp.append(final[-1][i] + final[-1][j])
                i+=1
                j+=1
            temp.append(1)
            final.append(temp)
            temp = [1]
            count+=1
        return final