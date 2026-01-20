'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        max_right = [0]
        max_left = [0]
        max_height = height[0]
        for i in range(1,len(height)):
            max_left.append(max_height)
            if height[i] >max_height:
                max_height = height[i]
        max_height = height[-1]
        for i in range(len(height)-2,-1,-1):
            max_right.insert(0,max_height)
            if height[i] >max_height:
                max_height = height[i]
        # print(max_left)
        # print(max_right)
        count =0
        for i in range(len(height)):
            final = min(max_left[i],max_right[i]) - height[i]
            if final>0:
                count+=final
        return count