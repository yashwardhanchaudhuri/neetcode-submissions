from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.mapping = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if not (self.mapping[key]):
            return ""

        left, right = 0, len(self.mapping[key]) - 1
        best_answer = ""

        while left <= right:
            mid = left + (right - left)//2
            if self.mapping[key][mid][1] == timestamp:
                return self.mapping[key][mid][0]

            if self.mapping[key][mid][1] < timestamp:
                best_answer = self.mapping[key][mid][0]
                left = mid + 1
            elif self.mapping[key][mid][1] > timestamp:
                right = mid - 1
            
        return best_answer