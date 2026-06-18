class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = [False] * 9
        # row validity check
        for row in board:
            for num in row: 
                if num == ".":
                    continue
                if seen[int(num) - 1]:
                    return False
                else: seen[int(num) - 1] = True
            seen[:] = [False] * 9
        # col validity check
        for idx in range(9):
            col = [row[idx] for row in board]
            for num in col:
                if num == ".":
                    continue
                if seen[int(num)-1]:
                    return False
                else: seen[int(num) - 1] = True
            seen[:] = [False] * 9
        # sub-box validity check
        for row in range(0,9,3):
            for col in range(0,9,3):
                sub_box = board[row][col:col + 3] + board[row + 1][col:col + 3] + board[row + 2][col:col + 3]
                for num in sub_box: 
                    if num == ".":
                        continue
                    if seen[int(num) - 1]:
                        return False
                    else: seen[int(num) - 1] = True
                seen[:] = [False] * 9
        return True
            