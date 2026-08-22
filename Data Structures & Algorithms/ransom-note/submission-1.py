class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = Counter(magazine)
        ransom = Counter(ransomNote)

        for r in ransomNote:
            if r not in mag or mag[r] < ransom[r]:
                return False
        return True