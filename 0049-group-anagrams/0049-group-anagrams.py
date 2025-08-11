class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list) # ord count: [words]
        for word in strs:
            count = [0] * 26
            for w in word:
                count[ord(w) - ord('a')] += 1
            hashmap[tuple(count)].append(word)
        
        return [ele for ele in hashmap.values()]