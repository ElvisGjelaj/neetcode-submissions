class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, (len(matrix) * len(matrix[0]) - 1)
        row_len = len(matrix[0])
        col_len = len(matrix)
        while l <= r:
            m = (l + r) // 2
            m_r = m // row_len
            m_c = m % row_len
            if matrix[m_r][m_c] > target:
                r = m_r * row_len + m_c - 1
            elif matrix[m_r][m_c] < target:
                l = m_r * row_len + m_c + 1
            else: return True
        return False