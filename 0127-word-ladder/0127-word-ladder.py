class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        nei = defaultdict(list)
        wordList.append(beginWord)

        # hashmap => O(n*m)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                nei[pattern].append(word)
        
        # print(nei)
        cnt = 1
        queue = deque([beginWord])
        seen = set([beginWord])
        while queue:
            # one stage
            for _ in range(len(queue)):
                word = queue.popleft() # target word
                
                # answer
                if word == endWord:
                    return cnt
                # track neighbor words
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in seen:
                            queue.append(neiWord)
                            seen.add(neiWord)
            cnt += 1

        return 0