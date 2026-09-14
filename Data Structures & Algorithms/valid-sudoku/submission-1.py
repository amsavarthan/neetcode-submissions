class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row=defaultdict(list)
        col=defaultdict(list)
        grid=defaultdict(list)

        for r in range(len(board)):
            for c in range(len(board)):
                num = board[r][c]
                if num == ".": continue

                # outer grid -> consider 3 row and 3 col bigger grid
                # since 9x9 there will be 3 col and rows in a single grid
                # for a pos (4,4) we divide by 3 to get bigger grid idx
                # (3,3) maps to (1,1) outer grid.

                gridIdx = str(r//3)+','+str(c//3)

                if num in row[r] or num in col[c] or num in grid[gridIdx]:
                    return False
                    
                row[r].append(num)
                col[c].append(num)
                grid[gridIdx].append(num)

        return True