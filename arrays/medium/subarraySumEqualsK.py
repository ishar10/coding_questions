'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums1 = [nums[0]]
        for i in range(1,len(nums)):
            nums1.append(nums1[i-1] +nums[i])
        hashmap = {0:1}
        count = 0
        for i in range(len(nums1)):
            if nums1[i]-k in hashmap:
                count += hashmap[nums1[i]-k]
            if nums1[i] in hashmap:
                hashmap[nums1[i]] +=1
            else:
                hashmap[nums1[i]] = 1
        return count




        