class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Map = collections.defaultdict(list) # count: [words]
        for word in strs:
            cnt = [0] * 26
            for c in word:
                cnt[ord(c)-ord('a')] += 1
            Map[tuple(cnt)].append(word)

        return [ words for words in Map.values()]