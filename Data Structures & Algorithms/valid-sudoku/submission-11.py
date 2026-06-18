class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sub_boxes = defaultdict(set)

        for row in range(0,9):
            for col in range(0,9):
                val = board[row][col]
                if val == ".":
                    continue
                elif val in rows[row]:
                    return False
                elif val in cols[col]:
                    return False
                elif val in sub_boxes[(row//3, col//3)]:
                    return False
                else:
                    rows[row].add(val)
                    cols[col].add(val)
                    sub_boxes[(row//3, col//3)].add(val)
        return True
        