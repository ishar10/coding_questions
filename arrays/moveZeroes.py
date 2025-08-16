'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 1
        while(j<len(nums)):
            if nums[i] == 0 and nums[j]!=0:
                t = nums[i]
                nums[i] = nums[j]
                nums[j] = t
                i+=1
                j+=1
            else:
                if nums[i] ==0 and nums[j] == 0:
                    j+=1
                elif nums[i]!=0 and nums[j]!=0:
                    i = j+1
                    j = i+1
                else:
                    i+=1
                    j+=1
        