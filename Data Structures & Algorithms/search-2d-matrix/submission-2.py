class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened = []
        for row in matrix:
            for num in row:
                flattened.append(num)
        l, r = 0, len(flattened) - 1
        while l <= r:
            mid = (l + r) // 2
            if flattened[mid] == target:
                return True
            elif flattened[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False