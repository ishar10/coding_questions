'''Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109 '''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 1
        i = 0
        j = i+1
        nums= sorted(nums)
        count = 1
        while(j<len(nums)):
            if nums[j] == (nums[i]+1):
                count+=1
                i+=1
                j+=1
            elif nums[i] == nums[j]:
                i+=1
                j+=1
            else:
                if count > max_length:
                    max_length = count
                count = 1
                i+=1
                j+=1
        if count>max_length:
            max_length = count
        if len(nums) ==0:
            return 0
        else:
            return max_length
        