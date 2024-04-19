class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append([value , timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.dic.get(key , [])
        left , right = 0 , len(values) - 1
        while left <= right :
            mid = (left + right) >> 1
            if values[mid][1] <= timestamp:
                left = mid + 1
                result = values[mid][0]
            else:
                right = mid - 1
        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)