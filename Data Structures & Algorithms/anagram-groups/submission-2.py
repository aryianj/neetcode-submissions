class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count: List[int] = [0] * 26
            for c in s:
                # get the frequency of each char in str
                count[ord(c) - ord('a')] += 1
            # append each str that has the same count
            res[tuple(count)].append(s)
        return list(res.values())