"""
    approach) Trie + backtracking
    1. make Trie dictionary using "words"
    2. track board using dfs(+backtracking) 
        and check whether current word is in the Trie dictionary
"""

class TrieNode:
    ## make Trie Dictionary
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution(object):
    # check current word is in the trie dictionary
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = TrieNode()
        
        # make trie dictinary
        for word in words:
            root.addWord(word)

        # check using dfs + backtracking
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            # base case
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]
            
            if node.isWord:
                res.add(word)

            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            visit.remove((r, c)) # backtracking

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "") # every point can be a starting point
        return list(res)