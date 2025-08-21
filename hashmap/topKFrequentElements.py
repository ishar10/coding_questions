'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        nums = sorted(nums)
        count = 1
        element = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == element:
                count +=1
                if i == len(nums)-1:
                    if count in hashmap:
                        hashmap[count].append(nums[i])
                    else:
                        hashmap[count] = [nums[i]]
            else:
                if count in hashmap:
                    hashmap[count].append(nums[i-1])
                else:
                    hashmap[count] = [nums[i-1]]
                count = 1
                element = nums[i]
            if i == len(nums)-1 and count == 1:
                if count in hashmap:
                    hashmap[count].append(nums[i])
                else:
                    hashmap[count] = [nums[i]]

        if len(nums) == 1:
            return nums
        else:
            print(hashmap)
            final = []
            for key, value in sorted(hashmap.items(), reverse = True):
                if k == len(value):
                    return final + value
                elif k < len(value):
                    return final + value[0:k]
                else:
                    final = final + value
                    k = k - len(value)