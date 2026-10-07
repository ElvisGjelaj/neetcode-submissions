class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sub_boxes = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                
                if val == ".":
                    continue
                elif val in rows[r] or val in cols[c] or val in sub_boxes[(r//3,c//3)]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                sub_boxes[(r//3,c//3)].add(val)
        
        return True

       
                
    
