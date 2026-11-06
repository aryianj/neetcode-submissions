class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lett = [0] * 26

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            lett[ord(s[i]) - ord('a')] += 1
            lett[ord(t[i]) - ord('a')] -= 1

        lett = [x for x in lett if x > 0]

        return len(lett) == 0

