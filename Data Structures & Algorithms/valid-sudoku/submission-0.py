class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[[""]*len(board) for i in range(len(board))]
        cols=[[""]*len(board) for i in range(len(board))]
        grids=[[] for i in range(len(board))]

        gridStart = [
                        (0,0),(0,3),(0,6),
                        (3,0),(3,3),(3,6),
                        (6,0),(6,3),(6,6)
                    ]

        for i in range(len(board)):
            for j in range(len(board)):
                rows[i][j]=board[i][j]
                cols[i][j]=board[j][i]
        
        for idx, (startI, startJ) in enumerate(gridStart):
            for i in range(startI,startI+3):
                for j in range(startJ, startJ+3):
                    grids[idx].append(board[i][j])

        return self.isValid(rows) and self.isValid(cols) and self.isValid(grids)
    
    def isValid(self, lists:List[List[str]])->bool:
        for lst in lists:
            nonDup=set()
            for num in lst:
                if num==".":
                    continue
                if num in nonDup:
                    return False
                else:
                    nonDup.add(num)
        return True
