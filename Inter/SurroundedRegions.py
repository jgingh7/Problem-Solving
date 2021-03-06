# https://leetcode.com/problems/surrounded-regions/
# Time: O(n)
# Space: O(n)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                self.dfs(board, 0, i)
                
        for i in range(len(board[0])):
            if board[-1][i] == 'O':
                self.dfs(board, len(board) - 1, i)
 
        for i in range(1, len(board) - 1):
            if board[i][0] == 'O':
                self.dfs(board, i, 0)
                
        for i in range(1, len(board) - 1):
            if board[i][-1] == 'O':
                self.dfs(board, i, len(board[0]) - 1)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'

        
        
    def dfs(self, board: List[List[str]], i: int, j: int):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != 'O':
            return
        
        board[i][j] = '#'
        
        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j + 1)
        self.dfs(board, i, j - 1)
