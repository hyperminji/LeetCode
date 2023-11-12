class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        answer=[]
        n=len(nums)
        for key,value in count.items():
            if value>(n//3):
                answer.append(key)
        return answer        
        