class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        hashmap = {}
        for i in range(len(nums)):
            if stack ==[]:
                stack.append((i,nums[i]))
            else:
                while(stack!=[] and stack[-1][1]<nums[i]):
                    hashmap[stack[-1][0]] = nums[i]
                    stack.pop()
                stack.append((i,nums[i]))
        if stack!=[]:
            for i in range(len(nums)):
                if stack ==[]:
                    break
                else:
                    while(stack !=[] and stack[-1][1] <nums[i]):
                        hashmap[stack[-1][0]] = nums[i]
                        stack.pop()
        num = nums
        for i in range(len(nums)):
            if i in hashmap:
                num[i] = hashmap[i]
            else:
                num[i] = -1
        return num