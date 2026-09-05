class MinStack:
    def __init__(self):
        self.storage = []
        self.mins = []

    def push(self, val: int) -> None:
        self.storage.append(val)
        if not self.mins or val <= self.mins[-1]:
            self.mins.append(val)
        else:
            self.mins.append(self.mins[-1])

    def pop(self) -> None:
        self.storage.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.storage[-1]

    def getMin(self) -> int:
        return self.mins[-1]