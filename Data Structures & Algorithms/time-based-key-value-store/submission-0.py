class TimeMap:

    def __init__(self):
        self.m = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.m[key]) - 1
        while l <= r:
            m = (l + r) // 2
            timestamp_m = self.m[key][m][0]
            if timestamp_m < timestamp:
                l = m + 1
            elif timestamp_m > timestamp:
                r = m - 1
            else:
                return self.m[key][m][1]
        return self.m[key][r][1] if r != -1 else ""