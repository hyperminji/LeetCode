class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod=10**9+7
        answer=0
        count=collections.Counter()
        for num in nums:
            num-=int(str(num)[::-1])
            answer+=count[num]
            count[num]+=1
        return answer%mod     
        