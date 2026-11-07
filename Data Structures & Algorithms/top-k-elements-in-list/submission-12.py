class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # {num[i]: occ} 
        map = defaultdict(int)

        # O(N)
        for num in nums:
            map[num]+=1

        topK = {k: v for k, v in sorted(map.items(), key=lambda item: item[1], reverse=True)}
        return list(topK.keys())[:k]
