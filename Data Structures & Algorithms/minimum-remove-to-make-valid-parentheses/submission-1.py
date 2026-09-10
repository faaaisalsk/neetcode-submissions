class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        cnt = 0
        for c in s:
            if c == '(':
                res.append(c)
                cnt +=1
            elif c == ')' and cnt > 0:
                res.append(c)
                cnt -=1
            elif c != ')':
                res.append(c)
        
        filtered = []
        for n in res[::-1]:
            if n == '(' and cnt > 0:
                cnt -=1
            else:
                filtered.append(n)
        return "".join(filtered[::-1])