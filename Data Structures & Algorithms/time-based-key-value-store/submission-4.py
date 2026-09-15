class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = [(value, timestamp)]
        else:
            self.timemap[key].append((value,timestamp))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ''
        else:
            if timestamp >= self.timemap[key][-1][1]:
                return self.timemap[key][-1][0]
            else:
                l, r = 0, len(self.timemap[key]) - 1

                while l <= r:
                    m = (l + r) // 2
                    if self.timemap[key][m][1] == timestamp:
                        return self.timemap[key][m][0]
                    if timestamp > self.timemap[key][m][1]:
                        l = m + 1
                    else:
                        r = m - 1

                # FIX: Return the value at index r, or '' if r went out of bounds
                return self.timemap[key][r][0] if r >= 0 else ''



