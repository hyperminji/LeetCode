class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = { char:num for num, char in enumerate(s)}
        start = 0
        right = 0
        result=[]
        for num, char in enumerate(s):
            right= max(right, dic[char])
            if right == num:
                result.append(right - start +1 )
                start = num + 1
        return result
        