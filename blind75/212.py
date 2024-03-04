class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False
    
    def add_word(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isword = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # add words in trie
        root = TrieNode()
        for w in words: root.add_word(w)
        
        # perform dfs backtracking
        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or ((r, c) in visited)
            or board[r][c] not in node.children):
                return False
            
            visited.add((r, c))

            node = node.children[board[r][c]]
            word = word + board[r][c]
            if node.isword: res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visited.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, '')

        return list(res)