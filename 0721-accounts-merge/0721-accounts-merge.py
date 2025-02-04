class Union:
    def __init__(self):
        self.parent = {}
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union = Union()
        email_to_name = {}

        for account in accounts:
            user = account[0]
            first = account[1]
            for email in account[1:]:
                if email not in union.parent:
                    union.parent[email] = email
                union.union(first, email)
                email_to_name[email] = user
        
        merged = defaultdict(set)
        for email in email_to_name:
            root = union.find(email)
            merged[root].add(email)
        
        result = []
        for root, emails in merged.items():
            result.append([email_to_name[root]] + sorted(emails))
        return result
