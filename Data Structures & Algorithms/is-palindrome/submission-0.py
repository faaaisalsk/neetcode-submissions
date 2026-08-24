class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = ''.join(ch.lower() for ch in s if ch.isalnum())
        
        l = 0
        r = len(strs)-1

        while r > l:
            if strs[l] != strs[r]:
                return False
            l +=1
            r -=1
        return True