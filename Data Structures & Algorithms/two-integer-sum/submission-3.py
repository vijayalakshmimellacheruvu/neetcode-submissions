class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i , num in enumerate(nums):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff],i]
            else:
                hashmap[num] = i