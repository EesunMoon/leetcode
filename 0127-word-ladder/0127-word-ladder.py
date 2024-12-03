class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # base case
        if endWord not in wordList:
            return 0

        # n = len(wordList), m = len(word)
        # Every adjacent pair of words differs by a single letter
        ## => adjacent list
        # shortest transformation sequence
        ## => BFS

        # 1) adjacent pair -> O(n*m^2)
        adj = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                adj[pattern].append(word)
        
        # 2) BFS
        ## initialization: start to beginWord
        visited = set([beginWord])
        queue = deque([beginWord])
        res = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j]+"*"+word[j+1:]
                    for neiWord in adj[pattern]:
                        if neiWord not in visited:
                            visited.add(neiWord)
                            queue.append(neiWord)

            res += 1
        
        return 0