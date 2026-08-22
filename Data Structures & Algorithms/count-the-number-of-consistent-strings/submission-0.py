class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter = Counter(allowed)
        notmatch = 0
        for w in words:
            countc = defaultdict(int)
            for c in w:
                if c not in counter:
                    notmatch +=1
                    break
                countc[c] +=1

        return len(words)-notmatch
