class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter = [0]*26
        for c in magazine:
            magazine_counter[ord(c)-ord('a')]+=1
        for c in ransomNote:
            magazine_counter[ord(c)-ord('a')]-=1
            if magazine_counter[ord(c)-ord('a')]<0:
                return False
        return True
        