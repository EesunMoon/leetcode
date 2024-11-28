class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique = defaultdict(list) # domain: local
        cnt = 0
        
        for email in emails:
            # 1) seperate @ => local / domain
            idx = email.index("@")
            local = email[:idx]
            domain = email[idx+1:]

            # 2) apply rule in local address
            local = local.replace('.', "")
            if "+" in local:
                plus = local.index("+")
                local = local[:plus]

            # 3) check
            if local not in unique[domain]:
                unique[domain].append(local)
                cnt += 1

        return cnt