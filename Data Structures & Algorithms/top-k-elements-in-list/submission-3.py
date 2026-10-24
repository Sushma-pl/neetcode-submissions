class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        
        return [x[0] for x in freq[:k]]