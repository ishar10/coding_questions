'''
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i = 0
        j = 0
        forward_col =1
        backward_col = 0
        forward_row =0
        backward_row =0
        col_limit_forward = len(matrix[0])
        col_limit_backward = - 1
        row_limit_forward = len(matrix)
        row_limit_backward = 0
        hashmap = {}
        while(1):
            if (i,j) not in hashmap:
                hashmap[(i,j)] =0
            else:
                break
            if forward_col:
                print("forward col")
                if (j+1) == col_limit_forward:
                    forward_col =0
                    forward_row =1
                    if (i+1) == row_limit_forward:
                        hashmap[(i,j)] =0
                        break
                    else:
                        col_limit_forward-=1
                        i+=1
                else:
                    j+=1
            elif backward_col:
                print("backward col")
                print(j)
                if (j-1) == col_limit_backward:
                    print("here")
                    backward_row =1
                    backward_col =0
                    if (i-1) == row_limit_backward:
                        hashmap[(i,j)] =0
                        break
                    else:
                        print("here1")
                        col_limit_backward+=1
                        i-=1   
                else:
                    j-=1
            elif forward_row:
                print("forward row")
                if (i+1) == row_limit_forward:
                    forward_row =0
                    backward_col=1
                    if (j-1) == col_limit_backward:
                        hashmap[(i,j)] =0
                        break
                    else:
                        row_limit_forward-=1
                        j-=1
                else:
                    i+=1
            elif backward_row:
                print("backward row")
                if (i-1) == row_limit_backward:
                    forward_col =1
                    backward_row =0
                    if (j+1) == col_limit_forward:
                        hashmap[(i,j)] =0
                        break
                    else:
                        row_limit_backward+=1
                        j+=1
                else:
                    i-=1
        
            print(hashmap)
        final = []
        for key,value in hashmap.items():
            i = key[0]
            j = key[1]
            final.append(matrix[i][j])
        return final