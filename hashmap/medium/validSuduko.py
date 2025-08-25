'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
'''


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap = {"1":1,"2":1,"3":1,"4":1,"5":1,"6":1,"7":1,"8":1,"9":1}
        hashmap1 = hashmap.copy()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (board[i][j] != ".") and (board[i][j] not in hashmap1):
                    return False
                else:
                    if board[i][j] != ".":
                        del hashmap1[board[i][j]]
            hashmap1 = hashmap.copy()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (board[j][i] != ".") and  (board[j][i] not in hashmap1):
                    return False
                else:
                    if board[j][i] != ".":
                        del hashmap1[board[j][i]]
            hashmap1 = hashmap.copy()

        seen = {0:{},1:{},2:{},3:{},4:{},5:{},6:{},7:{},8:{}}
        for i in range(len(board)):
            for j in range(len(board[i])):
                if i <3 and j<3:
                    if board[i][j]!="." and board[i][j] in seen[0]:
                        return False
                    else:
                        if board[i][j]!=".":
                            seen[0][board[i][j]] = 1
                elif i <3 and j>=3 and j < 6:
                    if board[i][j]!="." and board[i][j] in seen[1]:
                        return False
                    else:
                        if board[i][j]!=".":
                            seen[1][board[i][j]] = 1
                elif i <3 and j >= 6:
                    if board[i][j]!="." and board[i][j] in seen[2]:
                        return False
                    else:
                        if board[i][j]!=".":
                            seen[2][board[i][j]] = 1

                if i >=3 and i<6 and j<3:
                    if board[i][j]!="." and board[i][j] in seen[3]:
                        return False
                    else:
                        if board[i][j]!=".":
                            seen[3][board[i][j]] = 1
                elif i >=3 and i<6 and j>=3 and j < 6:
                    if board[i][j]!="." and board[i][j] in seen[4]:
                        return False
                    else:
                        if board[i][j]!=".":
                            seen[4][board[i][j]] = 1
                elif i >=3 and i<6 and j >= 6:
                    if board[i][j]!="." and board[i][j] in seen[5]:
                        return False
                    else:
                        if board[i][j]!=".":
                            seen[5][board[i][j]] = 1

                if i >=6 and j<3:
                    if board[i][j]!="." and board[i][j] in seen[6]:
                        return False
                    else:
                        if board[i][j]!=".":
                            seen[6][board[i][j]] = 1
                elif i >=6 and j>=3 and j < 6:
                    if board[i][j]!="." and board[i][j] in seen[7]:
                        return False
                    else:
                        if board[i][j]!=".":
                            seen[7][board[i][j]] = 1
                elif i >=6 and j >= 6:
                    if board[i][j]!="." and board[i][j] in seen[8]:
                        return False
                    else:
                        if board[i][j]!=".":
                            seen[8][board[i][j]] = 1
                    
    
        return True