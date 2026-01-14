'''
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        max_length = 1
        for i in range(len(s)):
            left, right = i,i
            while(left>=0 and right <len(s) and s[left]== s[right] ):
                if (right-left+1) >max_length:
                    res = s[left:right+1]
                    max_length = right-left+1
                left-=1
                right+=1

            left , right = i,i+1
            while(left>=0 and right <len(s) and s[left]== s[right]):
                if (right-left+1) >max_length:
                    res = s[left:right+1]
                    max_length = right-left+1
                left-=1
                right+=1
        return res

