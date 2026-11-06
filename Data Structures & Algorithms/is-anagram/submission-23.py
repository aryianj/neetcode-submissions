class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        a: List[int] = [0] * 26
        for i in range(len(s)):
            chs: int = ord(s[i]) - ord('a')
            cht: int = ord(t[i]) - ord('a')

            a[chs] += 1
            a[cht] -= 1

        a = [x for x in a if x != 0]
        return len(a) == 0
