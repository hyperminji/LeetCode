class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        n = len(nums)
        avgs = [-1] * n

        if 2 * k + 1 > n:
            return avgs

        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

            
        for i in range(k, n - k):
            left, right = i - k, i + k
            sub_array_sum = prefix[right + 1] - prefix[left]
            avg = sub_array_sum // (2 * k + 1)
            avgs[i] = avg

        return avgs
        