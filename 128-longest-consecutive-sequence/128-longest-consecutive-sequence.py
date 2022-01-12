# set -> in으로 찾기
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        n_set = set(nums)
        
        for n in n_set:
            if n - 1 not in n_set:
                curr = n
                count = 1
                while curr + 1 in n_set:
                    curr += 1
                    count += 1
                result = max(result, count)
        return result
                
            
            
        