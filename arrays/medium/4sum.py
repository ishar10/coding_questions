'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
 
Discover more
Software
Programming
Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,542,193/3.9M
Acceptance Rate
39.6%

'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        final = []
        for i in range(len(nums)-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            target_to_three = target - nums[i]
            for j in range(i+1,len(nums)):
                if ((j-1) !=i) and nums[j] == nums[j-1]:
                    continue
                target_to_two = target_to_three - nums[j]
                left = j+1
                right = len(nums)-1
                while(left<right):
                    if (nums[left] +nums[right]) == target_to_two:
                        final.append([nums[i],nums[j],nums[left],nums[right]])
                        while(right > 0 and (nums[right] == nums[right-1])):
                            right-=1
                        while(left<(len(nums)-1) and (nums[left] == nums[left+1])):
                            left+=1
                        right-=1
                        left+=1
                    elif (nums[left] +nums[right]) > target_to_two:
                        while(right > 0 and (nums[right] == nums[right-1])):
                            right-=1
                        right-=1
                    else:
                        while(left<(len(nums)-1) and (nums[left] == nums[left+1])):
                            left+=1
                        left+=1
                        
                    
        return final
        