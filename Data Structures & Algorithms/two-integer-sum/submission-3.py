class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for idx, num in enumerate(nums):
            map[num]=idx
        
        for idx, num in enumerate(nums):
            if map.get(target-num) != None and map.get(target-num) != idx:
                return [idx, map[target-num]]