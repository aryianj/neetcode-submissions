class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr : list[int] = [0] * 26

        if len(s) != len(t):
            return False # can't be an anagram if length is different

        for i in range(len(s)):
            arr[ord(s[i]) - ord('a')] += 1
            arr[ord(t[i]) - ord('a')] -= 1

        for i in range(len(arr)):
            if arr[i] != 0:
                return False
        return True






