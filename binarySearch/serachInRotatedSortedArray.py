'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) ==1:
            return -1 if target not in nums else 0
        if len(nums) ==2:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
            return -1
        if nums[0] >nums[-1]:
            i =0
            j = i+1
            while(nums[i]<nums[j]):
                i+=1
                j+=1
                if j ==len(nums):
                    break
            nums1 = nums[0:i+1]
            l=0
            h = len(nums1) -1
            while(l<=h):
                m = (l+h)//2
                if nums1[m] == target:
                    return m
                elif nums1[m] > target:
                    h = m-1
                else:
                    l = m+1
            if j!= len(nums):
                nums2 = nums[j::]
                l=0
                h = len(nums2) -1
                while(l<=h):
                    m = (l+h)//2
                    if nums2[m] == target:
                        return len(nums1)+ m
                    elif nums2[m] > target:
                        h = m-1
                    else:
                        l = m+1

            return -1
        else:
            l=0
            h = len(nums) -1
            while(l<=h):
                m = (l+h)//2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    h = m-1
                else:
                    l = m+1
            return -1