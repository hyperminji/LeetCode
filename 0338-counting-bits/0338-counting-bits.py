class Solution:
    def countBits(self, n: int) -> List[int]:
        result=[]
        for i in range(n+1):
            bn= "{0:b}".format(i)
            if '1' not in bn:
                result.append(0)
            else:
                count=0
                for i in bn:
                    if i == '1':
                        count +=1
                result.append(count)

        return result
        