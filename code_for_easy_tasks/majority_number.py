from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        result = 0
        majority = 0
        for num in nums:
            # 如果num在dict中，则num的数量加1，否则num的值为1（dict.get(num, 0)表示如果num在dict中，则返回num的值，否则返回0）
            dict[num] = dict.get(num, 0) + 1  
            # 如果num的数量大于majority，则将num的值赋给result，并将num的数量赋给majority
            if dict[num] > majority:
                majority = dict[num]
                result = num   
        return result
nums = [2,2,1,1,1,2,2]
majority = Solution()
a = majority.majorityElement(nums)
print(f"Majority element: {a}")
