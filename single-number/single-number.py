#pop -> append 
#중복이 되면 remove
#남은 것 return 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_list = []
        for i in nums:
            if i not in nums_list:
                nums_list.append(i)
            else:
                nums_list.remove(i)
        result= nums_list.pop()
        
        return result
        