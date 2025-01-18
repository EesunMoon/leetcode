class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode() # make new child node
            curr = curr.children[c]
        curr.word = True # mark as word

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # dfs: current index, current node
        def dfs(j, node):
            curr = node
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    # track all children of current node
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.word
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)