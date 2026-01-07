'''
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 

Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
'''
class Solution:
    def calculate(self, s: str) -> int: 
        s = s.replace(' ', '')
        if ' ' not in s and "+" not in s and "-" not in s and "(" not in s and ")" not in s:
            return int(s)
        stack =[[0,1]] # [last_result, sign]
        i =0
        while(i<len(s)):
            if s[i] =="(":
                stack.append([0,1])
                i+=1
            elif s[i] == ")":
                last = stack.pop()
                last_to_last = stack.pop()
                opr = last_to_last[1]
                num = 0
                if opr == 0:
                    num = last_to_last[0] - last[0]
                else:
                    num = last_to_last[0] +last[0]
                stack.append([num,1])
                i+=1
            elif s[i] == "+":
                stack[-1][1] = 1
                i+=1
            elif s[i] == "-":
                stack[-1][1] =0
                i+=1
            else:
                final_num = ""
                while(i<len(s) and s[i]!="(" and s[i]!=")" and s[i]!="+" and s[i]!= "-"):
                    final_num = final_num+s[i]
                    i+=1
                last = stack.pop()
                opr = last[1]
                num =0
                if opr ==1:
                    num = last[0] + int(final_num)
                else:
                    num = last[0] - int(final_num)
                stack.append([num,1])

        return stack[0][0]



            

        