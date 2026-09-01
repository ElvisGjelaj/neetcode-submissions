class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        curr = []

        def backtrack(r, coords):
            if r == n:
                curr.append(coords.copy())
                return

            for c in range(n):
                in_col = any(coord[1] == c for coord in coords)
                in_diag = any(
                    abs(coord[0] - r) == abs(coord[1] - c)
                    for coord in coords
                )

                if not in_col and not in_diag:
                    coords.append((r, c))
                    backtrack(r + 1, coords)
                    coords.pop()

        backtrack(0, [])

        for coords in curr:
            board = []

            for r, c in coords:
                row = ["."] * n
                row[c] = "Q"
                board.append("".join(row))

            res.append(board)

        return res