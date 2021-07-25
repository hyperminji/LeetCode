#find all case
# array num
#emu ->> all case 




class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        result = []
        for _ in range(len(nums)):
            num = nums.pop(0)
            perm_results = self.permute(nums)
            for perm in perm_results:
                perm.append(num)
            result = result + perm_results

            nums.append(num)
        return result