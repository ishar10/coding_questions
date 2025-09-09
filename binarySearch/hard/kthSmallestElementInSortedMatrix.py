'''
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2

'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        #time limit exceeds in this case:
        # stack = []
        # stack2 = []
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if stack !=[]:
        #             while(stack[-1]>matrix[i][j]):
        #                 stack2.insert(0,stack.pop())
        #             stack.append(matrix[i][j])
        #             stack = stack + stack2
        #             stack2 = []
        #         else:
        #             stack.append(matrix[i][j])
        # return stack[k-1]

        # binary search ( optimised)
        l = matrix[0][0]
        h = matrix[len(matrix)-1][len(matrix[0])-1]
        last_element = []
        for i in range(len(matrix)):
            last_element.append(matrix[i][-1])
        prev_mid = 'a'
        while(l<=h):
            
            mid = (l+h)//2
            print("low,high,mid",l,h,mid)
            count = 0
            for i in range(len(last_element)):
                if last_element[i] <= mid:
                    count += len(matrix[0])
                else:
                    j= 0
                    while(j<len(matrix[0])):
                        if matrix[i][j] <= mid:
                            count+=1
                            j+=1
                        else:
                            break
            print("count",count)
            
            if count > k and mid != prev_mid:
                h = mid
                prev_mid = mid
            elif count < k and  mid != prev_mid: 
                l = mid
                prev_mid = mid
            else:
                k1 =k
                if count <k:
                    mid = mid+1
                for i in range(len(last_element)):
                    j=0
                    print("one")
                    print("last_element, mid", last_element[i],mid)
                    if last_element[i] <= (mid):
                        print(len(matrix[0]),k)
                        k -= len(matrix[0])
                        print("k---", k)
                    else:
                        print("else",k)
                        while(j<len(matrix[0]) and k>0):
                            if matrix[i][j] <= mid:
                                print("i,j,k", i, j ,k)
                                k-=1
                                j+=1
                            else:
                                break
                    if k <=0:
                        final = []
                        for i1 in range(i+1):
                            final = final + matrix[i1]
                        final = sorted(final)
                        return final [k1-1]