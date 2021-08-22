class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums))]
        
        for num, freq in collections.Counter(nums).items():
            bucket[len(nums)-freq].append(num)
        
        answer = sum(bucket, [])[:k]    
        
        return answer
        