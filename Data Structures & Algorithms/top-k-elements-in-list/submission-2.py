from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map=defaultdict(int)
        for num in nums:
            map[num]+=1
        
        buckets=[[] for _ in range(len(nums))] # use comprehension for mutable types. normal []*num for immutable types
        
        for key in map.keys():
            value = map[key]-1
            buckets[value].append(key)

        res =[]
        for i in reversed(range(len(nums))):
            if len(buckets[i])>0:
                res=res+buckets[i]
        
        return [res[i] for i in range(k)]
            

        