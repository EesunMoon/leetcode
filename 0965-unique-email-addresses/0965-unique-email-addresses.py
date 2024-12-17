class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique = set()

        for email in emails:
            # 1) split the local name, domain name
            local, domain = email.split("@")

            # 2) [local name] "." <- remove
            # 3) [local name] "+":: remove everthing after + sign
            local = local.split("+")[0].replace(".", "")

            # 4) add in the set: local + domain
            unique.add(local+"@"+domain)
        
        return len(unique)
            
