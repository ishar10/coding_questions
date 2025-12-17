'''
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

 

Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1
 

Constraints:

1 <= n <= 231 - 1
'''

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s= str(n)
        i = len(s)-1
        s1 = ""
        s2 = s[-1]
        while(i>=1):
            if int(s[i-1])>=int(s[i]):
                s2 =  s[i-1]+ s2
            else:
                break
            i-=1
        s1 = s1 + s[:i]
        if s2 == s:
            return -1
        else:
            all = list(s2)[::-1]
            last_s1 = s1[-1]
            j = len(s2)-1
            temp_s2 = list(s2)
            for i in all:
                s1 = s1[:-1] + i
                temp_s2[j] = last_s1
                temp_s2 = "".join(temp_s2)
                final = int(s1+temp_s2[::-1])
                if final > n and final <= (2**31)-1:
                    return final
                
                j-=1
                temp_s2 = list(s2)
            
            return -1




            