'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k ==1:
            return nums
        queue = []
        final =[]
        for i in range(len(nums)):
            if i>=k:
                final.append(nums[queue[0]])
            if queue == []:
                queue.append(i)
            elif nums[queue[-1]] >= nums[i]:
                #last 0    i 3
                if queue[0]>(i-k): 
                    queue.append(i)
                else:
                    queue.pop(0)
                    queue.append(i)
            else:
                if queue[0]<=(i-k): 
                    queue.pop(0)
                while(queue and nums[queue[-1]]<nums[i]):
                    queue.pop(-1)
                queue.append(i)
            if i==len(nums)-1:
                final.append(nums[queue[0]])

        return final
            



                
                


                







        