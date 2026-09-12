from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #this solution can be done by adding (freq, num) tuple in maxheap
        #and popping k times.

        count=defaultdict(int)
        freq=[[] for _ in range(len(nums))]

        for num in nums:
            count[num]+=1
        
        for num, c in count.items():
            freq[c-1].append(num)
        
        res=[]
        for i in reversed(range(len(freq))):
            for num in freq[i]:
                if(len(res)==k):
                    break
                res.append(num)
        
        return res