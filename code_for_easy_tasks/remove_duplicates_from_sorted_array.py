from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                nums[i + 1] = nums[j]
                i = i + 1
        return i + 1
