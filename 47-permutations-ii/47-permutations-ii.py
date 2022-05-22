class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        
        def bkack(comb, counter):
            if len(comb) == len(nums):
                answer.append(list(comb))
                return
            
            for num in counter:
                if counter[num] >0:
                    comb.append(num)
                    counter[num] -= 1
                    bkack(comb, counter)
                    
                    comb.pop()
                    counter[num] += 1
                    
        bkack([], Counter(nums))
        
        return answer