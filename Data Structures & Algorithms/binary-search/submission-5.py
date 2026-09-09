class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:                    # <=, so the final element is checked
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1              # +1/-1, so the window always shrinks
            else:
                r = mid - 1
        return -1