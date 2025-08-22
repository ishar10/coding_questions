'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) >len(s):
            return []
        hashmap = {}
        final = []
        for i in p:
            if i in hashmap:
                hashmap[i] +=1
            else:
                hashmap[i] = 1
        hashmap1 = {}
        for i in range(len(p)):
            if s[i] in hashmap1:
                hashmap1[s[i]] +=1
            else:
                hashmap1[s[i]] =1
        if hashmap == hashmap1:
            final.append(0)
        
        if hashmap1[s[0]]>1:
            hashmap1[s[0]]-=1
        else:
            del hashmap1[s[0]]
        i = 1
        j = len(p)
        while(j<len(s)):
            if s[j] in hashmap1:
                hashmap1[s[j]] +=1
            else:
                hashmap1[s[j]] =1
            if hashmap == hashmap1:
                final.append(i)
            if hashmap1[s[i]]>1:
                hashmap1[s[i]]-=1
            else:
                del hashmap1[s[i]]
            i+=1
            j+=1
        return final