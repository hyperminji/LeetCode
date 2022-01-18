class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic ={}
        for key, value in enumerate(numbers):
            diff = target - numbers[key]
          
            if diff in dic:
                return[dic[diff]+1, key +1]
            else:
                dic[value] = key 
            
     