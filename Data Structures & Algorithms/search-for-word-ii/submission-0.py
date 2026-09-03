class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
        

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # makes the words trie
        root = TrieNode()

        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            
            curr.word = word

        # backtracking
        ROWS = len(board)
        COLS = len(board[0])
        res = []

        def dfs(r,c,curr_node):

            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            
            char = board[r][c]

            if char == "$":
                return
            
            if char not in curr_node.children:
                return
            
            next_node = curr_node.children[char]

            if next_node.word:
                res.append(next_node.word)
                next_node.word = None
            
            board[r][c] = "#"

            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)

            board[r][c] = char


        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)

        return res


        
         

        