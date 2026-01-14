'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) >len(haystack):
            return -1
        ln = len(needle)
        for i in range(len(haystack)):
            if len(needle) >len(haystack[i:]):
                return -1
            if haystack[i] == needle[0]:
                flag =0
                j = i+(ln -1)
                k = len(needle)-1
                while(j!=i):
                    if haystack[j]!= needle[k]:
                        flag =1
                        break
                    j-=1
                    k-=1
                if flag == 0:
                    return i
        return -1


        