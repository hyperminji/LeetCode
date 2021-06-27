class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_dic={}
        for i, val in enumerate(nums):
            if val in result_dic:
                return [result_dic[val],i]
            else:
                result_dic[target-val] = i
        