class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        counter = Counter(tops + bottoms)
        val, count = counter.most_common(1)[0]
        
        if count < len(tops):
            return -1
        
        if tops.count(val) < bottoms.count(val):
            tops, bottoms = bottoms, tops
        
        swap_count = 0
        
        for i in range(len(tops)):
            if tops[i] == val:
                continue
            if bottoms[i] == val:
                swap_count += 1
                continue
            return -1
        
        return min(swap_count, len(tops) - swap_count)
        