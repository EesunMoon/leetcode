class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique = set()
        
        for email in emails:
            # 1) seperate @ => local / domain
            local, domain = email.split("@")

            # 2) apply rule in local address
            local = local.split("+")[0].replace(".", "")

            # 3) check
            unique.add(local + "@" + domain)

        return len(unique)