class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        cntw = defaultdict(int)
        
        for w in words:
            for c in w:
                cntw[c] +=1

        for c in cntw:
            if cntw[c] % len(words):
                return False
        return True