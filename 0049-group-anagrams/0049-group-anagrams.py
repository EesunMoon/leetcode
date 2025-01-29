class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list) # (0, 1, ..., 0): [strs1, strs2, ..]

        for elem in strs:
            count = [0] * 26 # num of lowercase alaphabets
            for e in elem:
                count[ord(e)-ord("a")] += 1
            group[tuple(count)].append(elem)

        return [ elem for elem in group.values() ]