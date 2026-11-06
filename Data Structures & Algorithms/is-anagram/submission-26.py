class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha = [0] * 26

        if len(s) != len(t): return False

        for i in range(len(s)):
            alpha[ord(s[i]) - ord('a')] += 1
            alpha[ord(t[i]) - ord('a')] -= 1
        
        for i in alpha:
            if i != 0:
                return False
        return True

