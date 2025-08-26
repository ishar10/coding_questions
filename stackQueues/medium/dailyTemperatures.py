'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
1,408,424/2.1M
Acceptance Rate

'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        hashmap = {}
        arr = [(0,temperatures[0])]
        for i in range(1,len(temperatures)):
            while(temperatures[i] > arr[-1][1]):
                hashmap[arr[-1][0]] = i- arr[-1][0]
                del arr[-1]
                if arr == []:
                    break
            arr.append((i,temperatures[i]))
        for i in range(len(temperatures)):
            if i in hashmap:
                temperatures[i] = hashmap[i]
            else:
                temperatures[i] = 0
        return temperatures