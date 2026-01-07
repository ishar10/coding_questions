'''
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
'''

class Solution:
    def calculate(self, s: str) -> int:
        num = []
        opr = []
        flag = 1
        p1 = 0
        for i in s:
            if i!=" ":
                if i not in "+-/*":
                    if flag ==1:
                        if num==[]:
                            num.append(i)
                        else:
                            dig = num.pop()
                            num.append(str(dig)+i)
                    else:
                        num.append(i)
                    flag = 1
                else:
                    flag = 0
                    if i == "*" or i =="/":
                        p1+=1
                    opr.append(i)
        if p1!=0:
            i = 0
            while(i<len(opr)):
                if opr[i] == "*":
                    final_num = int(num[i]) * int(num[i+1])
                    num[i] = str(final_num)
                    num.pop(i+1)
                    opr.pop(i)
                    p1-=1
                elif opr[i] == "/":
                    final_num = int(num[i]) // int(num[i+1])
                    num[i] = str(final_num)
                    num.pop(i+1)
                    opr.pop(i)
                    p1-=1
                else:
                    i+=1

                if p1 ==0:
                    break
        i =0
        if opr==[]:
            return int(num[0])
        while(i<len(num)):
            if opr[i] == "+":
                final_num = int(num[i]) + int(num[i+1])
                num[i] = str(final_num)
                num.pop(i+1)
                opr.pop(i)
            elif opr[i] == "-":
                final_num = int(num[i]) - int(num[i+1])
                num[i] = str(final_num)
                num.pop(i+1)
                opr.pop(i)
            else:
                i+=1
            if i>=len(opr):
                break

        return int(num[0])
        # return int(num.pop())

        