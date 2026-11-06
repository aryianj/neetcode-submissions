class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)

        for num in nums:
            m[num] += 1

        m = dict(sorted(m.items(), key=lambda item: item[1]))
        res = []
        for i in range(k):
            key, _ = m.popitem()
            res.append(key)
        return res
        
        