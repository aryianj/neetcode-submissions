class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=len)
        prefix = strs[0]

        for str in strs:
            while prefix not in str:
                prefix = prefix[:-1]
        return prefix