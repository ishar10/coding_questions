'''
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count =0
        if len(s) ==0:
            return max_count
        queue = []
        unique = {}
        count =0
        for i in range(len(s)):
            if s[i] not in unique:
                unique[s[i]] =1 
                queue.append(s[i])
                count+=1
            else:
                if count >max_count:
                    max_count = count
                while(True):
                    if queue[0] in unique:
                        unique[queue[0]]-=1
                        if unique[queue[0]] ==0:
                            del unique[queue[0]]
                    e = queue.pop(0)
                    count-=1
                    if e == s[i]:
                        break
                queue.append(s[i])
                if s[i] in unique:
                    unique[s[i]] +=1
                else:
                    unique[s[i]] =1
                count+=1
        if count >max_count:
            max_count = count
        return max_count
