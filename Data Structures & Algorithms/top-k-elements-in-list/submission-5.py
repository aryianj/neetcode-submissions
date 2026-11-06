import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp : dict = {}
        for val in nums:
            mp[val] = mp.get(val, 0) + 1        
        
        pq : List[int] = []
        for key, freq in mp.items():
            heapq.heappush(pq, [freq, key])

            if len(pq) > k:
                heapq.heappop(pq)
        
        res : List[int] = []
        temp : List[int] = [0] * len(pq)
        index : int = len(pq) - 1

        while pq:
            temp[index] = heapq.heappop(pq)[1]
            index -= 1
        for val in temp:
            res.append(val)

        return res

        
