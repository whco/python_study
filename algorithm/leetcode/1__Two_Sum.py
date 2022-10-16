class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = dict()
        for i, num in enumerate(nums):
            if target - num in num_to_index:
                return [i, num_to_index[target - num]]
            num_to_index[num] = i