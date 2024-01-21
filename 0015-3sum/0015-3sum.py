class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result= set()
        
        n,p,z = [],[],[]
        
        for num in nums:
            if num>0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)
        
        setn, setp = set(n),set(p)
        
        if z:
            for num in setp:
                if -1*num in setn:
                    result.add((-1*num,0,num))
                    
        if len(z) >=3:
            result.add((0,0,0))
        
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in setp:
                    result.add(tuple(sorted([n[i],n[j],target])))
        
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in setn:
                    result.add(tuple(sorted([p[i],p[j],target])))
        return result
                    
