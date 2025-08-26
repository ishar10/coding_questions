'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in range(len(s)):

            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                l.append(s[i])
            else:
                if s[i] == ")":
                    if len(l) and l[-1] == "(":
                        del l[-1]
                    else:
                        return False 
                elif s[i] == "}":
                    if len(l) and l[-1] == "{":
                        del l[-1]
                    else:
                        return False 
                elif s[i] == "]":
              
                    if len(l) and l[-1] == "[":
               
                        del l[-1]
            
                    else:
                        return False 
        if not len(l):
            return True
        else:
            return False