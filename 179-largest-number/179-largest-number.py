#각 요소 단위로 크기순으로 정렬하면 됨 

class Solution:
    
    #문제에 적합한 비교 함수
    @staticmethod
    def to_swap(n1 : int, n2:int)-> bool:
        return str(n1) +str(n2) < str(n2)+str(n1)
        
    #삽입 정렬 구현
    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j>0 and self.to_swap(nums[j-1], nums[j]):
                nums[j], nums[j-1]= nums[j-1], nums[j]
                j = j-1
            i = i+1
            
        return str(int(''.join(map(str, nums)))) #join()결과를 int로 바꿔서 00->0 되도록 처리
        