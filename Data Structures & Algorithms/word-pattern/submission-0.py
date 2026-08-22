class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordstochar = {}
        chartowords = {}

        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        for p, s in zip(pattern, words):
            if p in wordstochar and wordstochar[p] != s:
                return False
            if s in chartowords and chartowords[s] != p:
                return False
            wordstochar[p] = s
            chartowords[s] = p
        return True

        