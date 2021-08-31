class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}
        
        for i in range(len(strs)):
            x = ''.join(sorted(strs[i]))
            if x not in dic:
                dic[x] = [strs[i]]
            else:
                dic[x].append(strs[i])
                
        return dic.values()