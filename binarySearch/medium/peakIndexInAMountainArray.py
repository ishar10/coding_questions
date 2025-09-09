'''
You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity.

 

Example 1:

Input: arr = [0,1,0]

Output: 1

Example 2:

Input: arr = [0,2,1,0]

Output: 1

Example 3:

Input: arr = [0,10,5,2]

Output: 1

 

Constraints:

3 <= arr.length <= 105
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.
'''
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        #complexity - n
        index = len(arr)-1
        i = index -1
        while(i>=0):
            if arr[i] > arr[i+1]:
                i = i-1
            else:
                return i+1
        
        #complexity - log(n)
        l =0
        r = len(arr)-1
        while(l<=r):
            mid = (l+r)//2
            if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
                return mid
            elif arr[mid] < arr[mid+1]:
                l = mid +1
            else:
                r = mid-1