'''Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
 

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,419,430/2.9M
Acceptance Rate
48.9%
'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack =[]
        stack.append((0,heights[0]))
        max_area = 0
        for i in range(1,len(heights)):
            if heights[i]>=heights[i-1]:
                stack.append((i,heights[i]))
            else:
                h = ()
                while(stack !=[] and stack[-1][1]>heights[i]):
                    h = stack.pop()
                    area = (i-h[0]) *h[1]
                    if area>max_area:
                        max_area = area
                stack.append((h[0],heights[i]))
        if stack!=[]:
            length = len(heights)
            while(stack!=[]):
                h = stack.pop()
                area = (length-h[0]) *h[1]
                if area > max_area:
                    max_area = area
        return max_area