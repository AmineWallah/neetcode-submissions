class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        thing = set()
        for num in nums:
            if num not in thing:
                thing.add(num)
            else: 
                return num
