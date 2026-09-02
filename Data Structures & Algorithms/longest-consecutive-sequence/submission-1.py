class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if not nums:
            return 0
        best = cur = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                cur += 1
                best = max(best, cur)
            else:
                cur = 1
        return best