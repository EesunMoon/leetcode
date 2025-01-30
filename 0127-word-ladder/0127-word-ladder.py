class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # base case
        if (endWord not in wordList):
            return 0
        
        # make wordDict - pattern: [word]
        wordDict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                keyword = word[:i] + "*" + word[i+1:]
                wordDict[keyword].append(word)
        
        # BFS - shortest path
        visit = set()
        queue = deque([beginWord])
        visit.add(beginWord)
        res = 0
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    res +=1
                    return res
                for i in range(len(word)):
                    keyword = word[:i] + "*" + word[i+1:]
                    for cand in wordDict[keyword]:
                        if (cand not in visit):
                            queue.append(cand)
                            visit.add(cand)
            res += 1
        return 0