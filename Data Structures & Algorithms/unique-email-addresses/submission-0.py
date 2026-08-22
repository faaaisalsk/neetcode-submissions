class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailset = set()
        for e in emails:
            local,domain = e.split('@')
            local = local.split('+')[0]
            local = local.replace('.','')
            emailset.add(local + '@' + domain)
        return len(emailset)