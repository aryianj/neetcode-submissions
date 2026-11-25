class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ""
        i = 0
        while i < len(word1):
            word += word1[i]
            if i < len(word2):
                word += word2[i]
            i += 1
        if len(word2) > len(word1):
            word += word2[i:]
        return word
        