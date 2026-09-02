class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cleared = set(nums)
        if len(cleared) != len(nums):
            return True
        else:
            return False
        