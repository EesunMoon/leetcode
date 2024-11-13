class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        m,n = len(mat), len(mat[0])
        sold_cnt = {}
        for i in range(m):
            count = Counter(mat[i])
            sold_cnt[i] = count.get(1)
        
        return heapq.nsmallest(k, sold_cnt.keys(), key = sold_cnt.get)
        